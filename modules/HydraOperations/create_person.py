import requests
from modules.Token import Token
import json
import datetime

class CreatePerson():

    """
    Creating person at hydra billing
    api guide https://files.hydra-billing.com/api_documentation/persons/create_person.html
    """


    def __init__(self, first_name, last_name, second_name, sex_id, d_birth, doc_serial, doc_number, doc_date, doc_authority):
        self.data = {
            "person": {
                "n_opf_id": "None",
                "n_firm_id": 100,
                "vc_first_name": first_name,
                "vc_surname": last_name,
                "vc_second_name": second_name,
                "n_sex_id": sex_id,
                "vc_inn": "",
                "vc_doc_serial": doc_serial,
                "vc_doc_no": doc_number,
                "d_doc": doc_date,
                "vc_document": doc_authority,
                "d_birth": d_birth,
                "vc_birth_place": "Россия",
                "vc_pens_insurance": "",
                "vc_med_insurance": "",
                "n_citizenship_id": "None",
                "vc_kpp": "",
                "vc_rem": "",
                "n_subj_state_id": "",
                "vc_doc_department": "",
                "n_doc_auth_type_id": 2015,
            }
        }

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/persons/"
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        if (response.status_code == 201):

            return {"person_id" : response.json()['person']['n_person_id'],
                        "status_code": response.status_code,
                        "message": "Физическое лицо {} {} успешно создано".format(self.data['person']['vc_first_name'], self.data['person']['vc_surname']) }

        else:
            return {"message": 'Не удалось создать физическое лицо. Код ошибки: {}'.format(response.text)}