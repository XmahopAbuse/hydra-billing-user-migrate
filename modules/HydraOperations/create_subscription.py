import requests
from modules.Token import Token
import json
import datetime
from modules.CONST import Const
from modules.helpers import convert_with_time
import datetime

class CreateSubscrition():

    """
    Creating address for person at hydra billing
    """

    def __init__(self, service_name, account_id, object_id, contract_id, customer_id):
        service_id = self.get_service_id(service_name)
        self.customer_id = customer_id
        self.data = {
              "subscription": {
                  "n_service_id": service_id,
                  "n_account_id": account_id,
                  "n_object_id": object_id,
                  "n_contract_id": contract_id,
                  "d_begin": convert_with_time(datetime.datetime.now()),
              }
            }

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "rest/v2/subjects/customers/{}/subscriptions/".format(self.customer_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        if "5" in str(response.status_code):
            return {"message": "Не удалось добавить тариф", "response": response.text}
        else:
            return {"message": "Тариф добавлен", "response": response.json()}

    def update(self, sub_id):
        data = {
              "subscription": {
                  'n_service_state_id': 9159,
                  'vc_service_state_name': 'Услуга не оказывается (заблокирована вручную)',
              }
            }
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = "https://operator.mks-net.ru/rest/v2/subjects/customers/51607701/subscriptions/51901301/edit"
        response = requests.put(url=url, data=json.dumps(data), headers=headers, verify=False)
        return response.text

    def get_service_id(self, service_name):
        service_name = str(service_name).strip()
        if service_name == 'МКС 60':
            return Const.TARIFF_60M
        elif service_name == "МКС 100":
            return Const.TARIFF_100M
        elif service_name == "МКС 3":
            return Const.TARIFF_3M
        elif service_name == "МКС 60+ТВ":
            return Const.TARIFF_60MTV
        elif service_name == "МКС 100+ТВ":
            return Const.TARIFF_100MTV
        elif service_name == "Электранет ПП u50M/450р":
            return Const.TARIFF_50M_450R