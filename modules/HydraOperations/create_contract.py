import requests
from modules.Token import Token
import json
import datetime

class CreateContact():

    """
    Creating address for person at hydra billing
    """

    BASE_CONTRACT_ID = 53665701

    def __init__(self, customer_id, date):
        self.data = {
              "contract": {
                "n_doc_state_id": 4003,
                "n_doc_type_id": 1002,
                "n_workflow_id": 10021,
                "n_parent_doc_id": self.BASE_CONTRACT_ID,
                "d_doc": date,
                "d_begin": date,
                "n_provider_id": 100,
                "n_firm_id": 100,
              }
            }
        self.customer_id = customer_id

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/customers/{}/contracts".format(self.customer_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)

        if response.status_code == 201:
            contract_id = response.json()['contract']['n_doc_id']
            return {"contract_id" : contract_id,
                    "message": "Документ с id {} успешно создан".format(contract_id)}
        else:
            return {"message": "Не удалось создать документ",
                    "contract_id": "Null"}


    def update(self, contract_id):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/customers/{}/contracts/{}".format(self.customer_id, contract_id)
        response = requests.put(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        if response.status_code == 200:
            return {"message": "Договор установлен в статус Активно"}
        else:
            return {"message": "Не удалось найти договор"}
