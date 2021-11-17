import requests
import json

class Token():

    """
    Generating token to access to REST API
    """

    def generate_token(self):

        payload = {
                 "session": {
                 "login" : "YOUR_USERNAME",
                 "password": "YOUR_PASSOWRD",
                 }
                }
        headers = {"Content-Type" : "application/json"}
        response = requests.post(url=self.BASE_URL+"/rest/v2/login", data=json.dumps(payload), headers=headers, verify=False)
        TOKEN = response.json()['session']['token']
        return TOKEN