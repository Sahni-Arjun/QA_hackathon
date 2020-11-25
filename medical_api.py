"""
Class for api
"""
import requests
import ast

class ApiClass:
    """
    class for api
    """
    base_url = "https://sandbox-healthservice.priaid.ch"
    sandbox_auth_token = ""

    def get_symptoms(self):
        symptom_url = f'{self.base_url}/symptoms?token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(symptom_url)
        print(response.content)

    def get_diagnosis(self, symptom_id_list):
        """"""
        diagnosis_url = f'{self.base_url}/diagnosis?symptoms={str(symptom_id_list)}&gender=male&year_of_birth=2000&token={self.sandbox_auth_token}&language=en-gb'
        response = requests.get(diagnosis_url)
        response_str = response.content.decode("UTF-8")
        return ast.literal_eval(response_str)





