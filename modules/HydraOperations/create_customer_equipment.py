import requests
from modules.Token import Token
import json
import datetime

class CreateCustomerEquipment():

    """
    Creating customer equipment at hydra billing
    api guide https://files.hydra-billing.com/api_documentation/persons/create_person.html
    """


    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.data = {
              "equipment": {
                "n_good_id": 21501,
                "n_firm_id": 100,
              }
            }


    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/customers/{}/equipment".format(self.customer_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)

        if (response.status_code == 201):
            print("Оконечное оборудование создано")
            return response.json()['equipment']['n_object_id']


        else:
            print("Оконечное оборудование не удалось создать")
            print(response.text)
            return 0
