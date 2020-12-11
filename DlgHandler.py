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

    def handle_response(self, response):
        payload = response['payload']
        if 'messages' in payload:
            self.handle_message(payload['messages'])
        if 'qaAction' in payload:
            return self.handle_qa(payload['qaAction'])
        elif 'daAction' in payload:
            return self.handle_qa(payload['daAction'])

    def handle_message(self, m_action):
        for message in m_action:
            eprint(message['visual'][0]['text'])


    def handle_qa(self, qa_action):
        eprint(qa_action['message']['visual'][0]['text'])
        x = input()
        return x

    def handle_da(self, da_action):
        return da_action['data']

    def response_type(self, response):
        payload = response['payload']
        return list(payload.keys())

