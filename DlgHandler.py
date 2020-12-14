"""
class to handle the dlg responses
"""
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)



class DlgHandler:
    """
    look above
    """
    def handle_message(self, m_action):
        for message in m_action:
            eprint(message['visual'][0]['text'])


    def handle_qa(self, response):
        payload = response['payload']
        if 'messages' in payload:
            self.handle_message(payload['messages'])
        eprint(payload['qaAction']['message']['visual'][0]['text'])
        x = input()
        return (x,payload['qaAction']['message']['visual'][0]['text'])

    def handle_da(self, response):
        payload = response['payload']
        if 'messages' in payload:
            self.handle_message(payload['messages'])
        if 'data' in payload['daAction']:
            return payload['daAction']['data']
        return payload['daAction']['id']

    def response_type(self, response):
        payload = response['payload']
        return list(payload.keys())

    def get_qa_text(self, response):
        return response['payload']['qaAction']['message']['visual'][0]['text']


