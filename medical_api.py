"""
Class for api
"""
import requests
import ast
import unicodedata
import json

class ApiClass:
    """
    class for api
    """
    #base_url = "https://sandbox-healthservice.priaid.ch"
    base_url = "https://healthservice.priaid.ch"
    def __init__(self):
        self.sandbox_auth_token = open('auth.txt', 'r').readline()

    def get_symptoms(self):
        symptom_url = f'{self.base_url}/symptoms?token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(symptom_url)
        return response.content

    def get_symptom_id(self, name):
        data_string = open('all_symptoms.json', 'r').read().replace('\n', ' ')
        symptom_list = ast.literal_eval(data_string)
        for x in symptom_list:
            if x['Name'].lower() == name.lower():
                return x["ID"]

    def get_diagnosis(self, symptom_id_list, gender, yob):
        """"""

        diagnosis_url = f'{self.base_url}/diagnosis?symptoms={str(symptom_id_list)}&gender={gender.lower()}&year_of_birth={str(yob)}&token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(diagnosis_url)
        response_str = response.content.decode("UTF-8")
        normalized_str = unicodedata.normalize('NFKD', response_str).encode('ascii', 'ignore').decode("UTF-8")
        return ast.literal_eval(normalized_str)

    def get_issue_info(self, issue_id):
        issue_url = f'{self.base_url}/issues/{str(issue_id)}/info?token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(issue_url)
        response_str = response.content.decode("UTF-8")
        normalized_str = unicodedata.normalize('NFKD', response_str).encode('ascii', 'ignore').decode("ascii")
        return json.loads(normalized_str)

    def get_more_symptoms(self, symptom_id_list, gender, yob):
        url = f'{self.base_url}/symptoms/proposed?token={self.sandbox_auth_token}&language=en-gb&symptoms={str(symptom_id_list)}&gender={gender.lower()}&year_of_birth={str(yob)}'
        response = requests.get(url)
        response_str = response.content.decode("UTF-8")
        normalized_str = unicodedata.normalize('NFKD', response_str).encode('ascii', 'ignore').decode("UTF-8")
        return ast.literal_eval(normalized_str)


doctor = ApiClass()
print(doctor.get_symptom_id('memory gap'))
