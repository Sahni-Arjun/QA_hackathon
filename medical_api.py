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
    sandbox_auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFyanVuc2Fobmljb2xsZWdlQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiNzk0NSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0xMC0xMyIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNjA2NDI1MjA5LCJuYmYiOjE2MDY0MTgwMDl9.l44Edt7evULKv0xA8Dgs8gCdTlhx7QuBSmPKTM8cpmU"

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


