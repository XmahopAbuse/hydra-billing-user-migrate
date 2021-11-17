import requests
from modules.Token import Token
import json
import datetime

class CreateAccount():

    """
    Создание счета для физического лица
    api guide https://files.hydra-billing.com/api_documentation/persons/create_person.html
    """
    RUB_CODE_ID = 1044
    def __init__(self, user_id, customer_id):
        self.customer_id = customer_id

        self.data= {
            "account": {
                "n_currency_id": self.RUB_CODE_ID,
                "vc_code": user_id,
                "vc_name": user_id,
                "vc_account": user_id,
            }
        }

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "rest/v2/subjects/customers/{}/accounts".format(self.customer_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        if response.status_code == 201:
            return {"account_id": response.json()['account']['n_account_id'],
                    "message": "Счет для аккаунта лица {} создан".format(self.customer_id)}
        else:
            return "Не удалось создать счет для физического лица. Код ошибки: {}".format(response.text)