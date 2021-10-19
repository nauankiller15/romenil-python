import requests
from datetime import datetime

from django.core.exceptions import RequestAborted
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import Model


from romenil.variaveis_de_ambiente import APIKEY, PUBLICKEY, EMAIL_API

class Subscription(Model):

    cpf_cnpj = CharField(max_length=14)
    client_id = IntegerField()
    product_id = IntegerField()
    email = EmailField()
    contract_status = CharField(max_length=15)  
    atualizacao = DateField(auto_now=True)


class TokenEduzz(Model):

    token = CharField(max_length=200)
    token_valid_until = CharField(max_length=20)


class Eduzz:
    headers = {
        'token': ''
    }

    def __init__(self, cpf_cnpj: str):
        self.cpf_cnpj = cpf_cnpj.replace('.', '').replace('-', '')

    @property
    def ativo(self):
        contrato = self.select_contrato
        if contrato:
            pass

        return False


    def select_contrato(self):
        contrato = self.select_contrato_db()

        if contrato is None:
            self.set_headers()
            subscriptions = self.subscription_list()
            for subscription in subscriptions:
                if subscription['cpf_cnpj'] == self.cpf_cnpj and subscription['product_id'] == 1048167:
                    contrato = Subscription.objects.create(
                        cpf_cnpj = subscription['cpf_cnpj'],
                        client_id = subscription['client_id'],
                        product_id = subscription['product_id'],
                        email = subscription['email'],
                        contract_status = subscription['contract_status'],
                    )
                    break

        return contrato

    def get_token(self):
        payload = {'publickey': PUBLICKEY, 'apikey': APIKEY, 'email': EMAIL_API}
        rq = requests.post("https://api2.eduzz.com/credential/generate_token", params=payload)
        
        if rq.status_code == 200:

            dados = rq.json()

            token_valid_until = dados['data']['token_valid_until']
            token = dados['data']['token']

            return {'token': token, 'token_valid_until': token_valid_until}
    
    def select_token(self):
        agora = datetime.now()
        token = TokenEduzz.objects.last()
        if token == None or datetime.fromisoformat(token.token_valid_until) < agora:
            print('token', token)
            dados = self.get_token()
            token = TokenEduzz.objects.update_or_create(token, defaults={
                'token': dados['token'], 'token_valid_until': dados['token_valid_until']
                }
            )
        
        return token.token
    
    def set_headers(self):
        token = self.select_token
        self.headers['token'] = token

    def conect(self, url):
        rq = requests.get(url, headers=self.headers)
        
        if rq.status_code == 200:
            dados = rq.json()

            return dados
        
        raise RequestAborted

    def select_contrato_db(self):
        contrato = Subscription.objects.filter(cpf_cnpj=self.cpf_cnpj, product_id=1048167).last()

        return contrato

    def subscription_list(self):

        # product_id = 1048167
        print('subscription_list')
        dados = self.conect("https://api2.eduzz.com/subscription/get_contract_list")
        return dados['data']
    
    def get_contract(self, pk):

        dados = self.conect(f"https://api2.eduzz.com/subscription/{pk}")        
        return dados['data'] 
