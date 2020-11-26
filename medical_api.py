"""
Class for api
"""
import requests
import ast
import unicodedata


class ApiClass:
    """
    class for api
    """
    base_url = "https://sandbox-healthservice.priaid.ch"
    def __init__(self):
        self.sandbox_auth_token = open('auth.txt', 'r').readline()

    def get_symptoms(self):
        symptom_url = f'{self.base_url}/symptoms?token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(symptom_url)
        print(response.content)

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
        return ast.literal_eval(response_str)

    def get_issue_info(self, issue_id):
        issue_url = f'{self.base_url}/issues/{str(issue_id)}/info?token={self.sandbox_auth_token}&language=en-gb'
        #issue_url = f'{self.base_url}/issues/324/info?token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(issue_url)
        response_str = response.content.decode("UTF-8")
        return unicodedata.normalize('NFKD', response_str).encode('ascii', 'ignore')


