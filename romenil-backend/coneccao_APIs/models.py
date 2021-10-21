from django.db.models.fields import DateTimeField
import requests
from datetime import datetime, timedelta, timezone

from django.core.exceptions import RequestAborted
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import Model
from django.utils import timezone


from romenil.variaveis_de_ambiente import APIKEY, PUBLICKEY, EMAIL_API

class Subscription(Model):

    client_document = CharField(max_length=14)
    contract_id = IntegerField()
    client_id = IntegerField()
    product_id = IntegerField()
    client_email = EmailField()
    contract_status = CharField(max_length=15)  
    atualizado_em = DateTimeField(auto_now=True)


class TokenEduzz(Model):

    token = CharField(max_length=200)
    token_valid_until = CharField(max_length=20)


class Eduzz:
    headers = {
        'token': ''
    }

    def __init__(self, cpf_cnpj: str):
        self.client_document = cpf_cnpj.replace('.', '').replace('-', '')

    @property
    def ativo(self):
        contrato = self.select_contrato()
        
        if contrato is not None and contrato.contract_status.upper() == 'EM DIA':
            return True
        else:
            return False


    def select_contrato(self):
        contrato = self.select_contrato_db()

        if contrato is None:
            subscriptions = self.subscription_list()
            for subscription in subscriptions:
                if subscription['client_document'] == self.client_document and subscription['product_id'] == 1048167:
                    contrato = Subscription.objects.create(
                        client_document = subscription['client_document'],
                        contract_id = subscription['contract_id'],
                        client_id = subscription['client_id'],
                        product_id = subscription['product_id'],
                        client_email = subscription['client_email'],
                        contract_status = subscription['contract_status'],
                    )
                    break
       
        if contrato is not None and  contrato.atualizado_em < datetime.now(timezone.utc) - timedelta(days=2):
            dados_contrato = self.get_contract(contrato.contract_id)
            contrato.contract_status = dados_contrato['contract_status']
            contrato.save()
            print('contract save')
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
        token = TokenEduzz.objects.filter(id=1).last()
        if token == None or datetime.fromisoformat(token.token_valid_until) < agora:
            dados = self.get_token()
            token, criado = TokenEduzz.objects.update_or_create(id=1, defaults={
                'token': dados['token'], 'token_valid_until': dados['token_valid_until']
                }
            )
        
        return token.token
    
    def set_headers(self):
        token = self.select_token()
        self.headers['token'] = token

    def conect(self, url):
        self.set_headers()
        rq = requests.get(url, headers=self.headers)
        
        if rq.status_code == 200:
            dados = rq.json()

            return dados
        
        raise RequestAborted

    def select_contrato_db(self):
        contrato = Subscription.objects.filter(client_document=self.client_document, product_id=1048167).last()

        return contrato

    def subscription_list(self):

        dados = self.conect("https://api2.eduzz.com/subscription/get_contract_list")
        return dados['data']
    
    def get_contract(self, pk):
        
        dados = self.conect(f"https://api2.eduzz.com/subscription/get_contract/{pk}")      
        return dados['data'][-1]

    def get_cliente(self, pk):
        
        dados = self.conect(f"https://api2.eduzz.com/subscription/{pk}/client")        
        return dados['data'] 
