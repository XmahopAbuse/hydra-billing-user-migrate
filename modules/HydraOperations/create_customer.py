import requests
from modules.Token import Token
import json
import datetime

class CreateCustomer():

    """
    Создание абонента для физического лица
    """

    GROUP_ID = "40231101" # айди группы для частных лиц


    # неактивен - 1011, активен - 2011


    def __init__(self, person_id, code, comment, d_created):
        self.person_id = person_id
        self.data= {
                      "customer": {
                        "n_base_subject_id": person_id,
                        "vc_code": code,
                        "n_subj_group_id": self.GROUP_ID,
                        "vc_rem": "loyality bonus is {}%".format(comment),
                        "d_created": d_created,
                        "n_subj_state_id": 2011,
                      }
                    }

    def create(self):
        """Создание учетной записи"""

        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/customers/"
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        if response.status_code == 201:
            return {"customer_id": response.json()['customer']['n_customer_id'],
                    "message": "Аккаунт для физического лица {} создан".format(self.person_id)}
        else:
            return {"customer_id": None,
                    "message": "Не удалось создать аккаунт для физического лица. Код ошибки: {}".format(response.text)}

    def update(self, customer_id):

        """Установка статуса Активен"""

        data = {
            "customer": {
                "n_subj_state_id": 2011,
            }
        }


        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token.TOKEN)}
        url = Token.BASE_URL + "/rest/v2/subjects/customers/{}".format(customer_id)
        response = requests.put(url=url, data=json.dumps(data), headers=headers, verify=False)
        print(response.json())