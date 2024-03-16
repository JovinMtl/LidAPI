import requests


class ConsumePrincipal:
    """THis is to explore the Principal ViewSet"""
    def __init__(self) -> None:
        self.user = {
            'username' : 'jovin',
            'password' : 'done1234',
        }
        self.url = 'http://127.0.0.1:8002/jov/api/principal/receiveDepot/'

    def sendData(self):
        response = requests.post(url=self.url, data=self.user)
        print("la reponse est : ", response)
        return 0


jove = ConsumePrincipal()
print(jove.sendData())