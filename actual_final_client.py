"""
where the code for the final dialog will be
"""

from final_client import *
from client import *
from medical_api import ApiClass
from DlgHandler import DlgHandler

def print_issue(issue_data):
    for data in issue_data:
        eprint(f'{data}: {issue_data[data]}')

def main():
    program = Program()
    args = parse_args()
    doctor = ApiClass()
    handler = DlgHandler()
    with create_channel(args) as channel:
        response = program.intialize_connection(channel)
        x = handler.handle_qa(response)
        response = program.respond(user_input=x[0])
        response = program.handle_name(response)
        response = program.intialize_variables(response)
        x = handler.handle_qa(response)
        response = program.respond(user_input=x[0])
        while 'age' in handler.get_qa_text(response) or 'gender' in handler.get_qa_text(response):
            x = handler.handle_qa(response)
            response = program.respond(user_input=x[0])
        response = program.handle_symptoms(3, response)
        data = handler.handle_da(response)
        yob = 2020 - int(data['user_details']['age'])
        gender = data['user_details']['gender']
        symptoms = []
        for x in data['symptom_obj']:
            if data['symptom_obj'][x] != '0':
                symptoms.append(data['symptom_obj'][x])
        symptom_ids = [doctor.get_symptom_id(name) for name in symptoms]
        diagnosis = doctor.get_diagnosis(symptom_ids, gender, yob)
        eprint(f'Your most likely diagnosis is: {diagnosis[0]["Issue"]["Name"]}')
        eprint(f'Here is more info about {diagnosis[0]["Issue"]["Name"]}')
        print_issue(doctor.get_issue_info(diagnosis[0]["Issue"]["ID"]))

        eprint("Thank you for using Team WBNESU's medical diagnosis application! We wish you a pleasant day!")

if __name__ == '__main__':
    main()


