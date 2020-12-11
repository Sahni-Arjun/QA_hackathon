from client import *
from google.protobuf.struct_pb2 import Struct
from DlgHandler import DlgHandler


class Program:
    session_id = None
    stub = None
    payload_dict = {"requested_data": {
        "id": "DataAccess_01",
        "data": {
            "symptom_obj": {'s1': '1', 's2': '2', 's3': '3'},
            "returnCode": "0"
        }
    }}

    selector_dict = {
        "channel": "default",
        "language": "en-US",
        "library": "default"
    }

    def __init__(self):
        handler = DlgHandler()
        self.args = parse_args()
        self.model_ref_dict = {
            "uri": self.args.modelUrn,
            "type": 0
        }
        self.requested_data_struct = Struct()
        self.id= 'DataAccess_01'
        self.requested_data_struct.update({"symptom_obj": {'s1': '1', 's2': '2', 's3': '3'}})
        self.requested_data_struct.update({"returnCode": "0"})

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


    def main(self):
        handler = DlgHandler()
        with create_channel(self.args) as channel:
            self.intialize_connection(channel)
            # log.debug(f'Second request, passing in user input')
            response = self.respond(requested_id=self.id, requested_data_struct=self.requested_data_struct)
            for i in range(3):
                x = handler.handle_response(response)
                response = self.respond(user_input=x)
                x = handler.handle_response(response)
                response = self.respond(user_input=x)
            eprint(response)
            



if __name__ == '__main__':
    program = Program()
    program.main()