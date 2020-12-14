from client import *
from google.protobuf.struct_pb2 import Struct
from DlgHandler import DlgHandler

class Program:
    session_id = None
    stub = None

    selector_dict = {
        "channel": "default",
        "language": "en-US",
        "library": "default"
    }

    def __init__(self):
        self.handler = DlgHandler()
        self.args = parse_args()
        self.model_ref_dict = {
            "uri": self.args.modelUrn,
            "type": 0
        }

    def respond(self, user_input=None, requested_id=None, requested_data_struct=None):
        payload_dict = {
            "user_input": {
                "userText": user_input
            }
        }
        response, call = execute_request(self.stub,
                                         session_id=self.session_id,
                                         selector_dict=self.selector_dict,
                                         payload_dict=payload_dict,
                                         data=requested_data_struct,
                                         id=requested_id
                                         )
        assert call.code() == StatusCode.OK
        return response

    def create_proto_struct(self, data_list):
        s = Struct()
        for data in data_list:
            s.update(data)
        s.update({"returnCode": "0"})
        return s

    def intialize_connection(self, channel):
        self.stub = DialogServiceStub(channel)
        response, call = start_request(self.stub,
                                       model_ref_dict=self.model_ref_dict,
                                       session_id=None,
                                       selector_dict=self.selector_dict
                                       )
        self.session_id = read_session_id_from_response(response)
        assert call.code() == StatusCode.OK
        # log.debug(f'Initial request, no input from the user to get initial prompt')
        response = self.respond()
        return response

    def handle_symptoms(self, num_symptoms, response):
        x = self.handler.handle_qa(response)
        for i in range(num_symptoms):
            response = self.respond(user_input=x[0])
            if 'daAction' in self.handler.response_type(response):
                break
            x = self.handler.handle_qa(response)
            response = self.respond(user_input=x[0])
            if 'daAction' in self.handler.response_type(response):
                break
            x = self.handler.handle_qa(response)
        return response

    def handle_name(self, response):
        name = self.handler.handle_da(response)
        x = input()
        s = self.create_proto_struct([{"user_name": x}])
        return self.respond(requested_id=name, requested_data_struct=s)

    def intialize_variables(self, response):
        name = self.handler.handle_da(response)
        variables = [{'symptom_obj': {'s1': '0', 's2': '0', 's3': '0'}}, {'user_details': {'age': '0', 'gender': '0'}}]
        s = self.create_proto_struct(variables)
        return self.respond(requested_id=name, requested_data_struct=s)




