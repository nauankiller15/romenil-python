import requests

from django.db.models import Model
from django.db.models.fields import CharField
from django.utils import timezone

from django.core.exceptions import RequestAborted
from romenil.variaveis_de_ambiente import APIKEY, PUBLICKEY, EMAIL


class TokenEduzz(Model):

    token = CharField(max_length=200)
    token_valid_until = CharField(max_length=20)



class Eduzz:
    headers = {
        'token': ''
    }

    def __init__(self):
        agora = timezone.now()
        token = TokenEduzz.objects.last()

        if token == None:
            dados = self.get_token()
            TokenEduzz.objects.create(token=dados['token'], token_valid_until=dados['token_valid_until'])
        elif token.token_valid_until >= agora:
            dados = self.get_token()
            token.token = dados['token']
            token.token_valid_until = dados['token_valid_until']
            token.save()


    def get_token(self):
        print('set_token')
        payload = {'publickey': PUBLICKEY, 'apikey': APIKEY, 'email': EMAIL}
        rq = requests.post("https://api2.eduzz.com/credential/generate_token", params=payload)
        
        if rq.status_code == 200:

            dados = rq.json()
            print(dados)

            token_valid_until = dados['data']['token_valid_until']
            token = dados['data']['token']
            self.headers['token'] = token
            
            return {'token': token, 'token_valid_until': token_valid_until}


    def subscription_list(self):
        # product_name
        print('subscription_list')
        dados = self.conect("https://api2.eduzz.com/subscription/get_contract_list")
        return dados['data'] 
        

    def get_contract(self, pk):

        dados = self.conect(f"https://api2.eduzz.com/subscription/{pk}")        
        return dados['data'] 


    def conect(self, url):
        rq = requests.get(url, headers=self.headers)
        
        if rq.status_code == 200:
            dados = rq.json()
            print(dados)

            return dados
        else:
            # melhorar levantamento de excessão
            raise RequestAborted
