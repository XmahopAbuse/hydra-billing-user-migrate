import requests
from modules.Token import Token
import json
import datetime

class CreateAddress():

    """
    Creating address for person at hydra billing
    """


    def __init__(self, person_id):
        self.data = {
              "address": {
                "n_addr_type_id": 1006,
                "n_subj_addr_type_id": 1016,
                "n_region_id": 51035201,
                "vc_address": "Россия, г. Москва, г. Зеленоград",
                "n_addr_state_id": 1029
              }
            }
        self.person_id = person_id

    def create(self):
        headers = {"Accept": "application/json", "Content-Type": "application/json",
                   "Authorization": "Token token={}".format(Token().generate_token())}
        url = Token.BASE_URL + "/rest/v2/subjects/persons/{}/addresses/".format(self.person_id)
        response = requests.post(url=url, data=json.dumps(self.data), headers=headers, verify=False)
        print(response.text)
        print(response.status_code)


a = CreateAddress()
a.create()