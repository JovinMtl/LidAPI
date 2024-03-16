import requests
import json
from django.http import JsonResponse, response, HttpResponse



class LumiRequest:
    """THis is for browsing the api of Lumi"""
    def __init__(self, receiver_number='62111333', \
                 amount_to_send='500') -> None:
        self.data_mine = {
            'owner_name': 'Lde',
            'owner_phone_number': '68111222',
            'password' : 'done1234',
            'receiver_number': receiver_number,
            'amount_to_send' : amount_to_send,
        }
        self.data_client = {
            'owner_name': 'client1',
            'owner_phone_number': '',
            'password' : 'done1234',
        }
        self.response = requests.models.Response()
        self.urlPower = "http://127.0.0.1:8002/power/solde/"

    def mySolde(self, action='get'):
        if action == 'transfer':
            self.urlPower = "http://127.0.0.1:8002/power/transfer/"
        self.response = requests.post(self.urlPower, self.data_mine)
        if self.response.status_code == 200:
            # return JsonResponse(self.response.json())
            return self.response
        return f"Failed"

    def clSolde(self):
        pass

# jov = LumiRequest()
# print(jov.mySolde('transfer'))