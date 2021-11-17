import requests
from modules.Token import Token
import json
import datetime

class CreateEntry():

    """
    Creating network services and attach it to user's end network device at hydra billing
    api guide https://files.hydra-billing.com/api_documentation/persons/create_person.html
    """


    def __init__(self, device_id):
        self.device_id = device_id
        self.data = {
  "entry": {
    "vc_code": "1",
    "vc_name": "Сетевой порт №1",
    "vc_code_add": "None",
    "vc_serial": "None",
    "vc_inv_no": "None",
    "n_catalog_item_id": 40249001,
    "n_firm_id": 100,
    "n_obj_state_id": 1040,
    "n_main_object_id": device_id
  }
}

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "rest/v2/objects/net_devices/{}/entries".format(self.device_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)

        if (response.status_code == 201):
            print("Компонент оконечного оборудования создан")
            return response.json()


        else:
            print("Не удалось создать компонент оконечного оборудования")
            print(response.text)
            return 0
