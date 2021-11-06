import requests
from datetime import datetime, timedelta, timezone

from django.core.exceptions import RequestAborted
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import Model
from django.utils import timezone


from romenil.variaveis_de_ambiente import APIKEY, PUBLICKEY, EMAIL_API

class Sale(Model):

    client_document = CharField(max_length=14)
    sale_id = IntegerField()
    content_id = IntegerField()
    client_email = EmailField()
    sale_status = IntegerField()
    atualizado_em = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client_email} - {self.client_document}'
    


class TokenEduzz(Model):

    token = CharField(max_length=200)
    token_valid_until = CharField(max_length=20)


class Eduzz:
    """Classe que faz a conexão e verificação de compra na API da Eduzz"""

    headers = {
        'token': ''
    }
    content_ids = (1048167, 1048227, 1048233, 1048233)

    def __init__(self, cpf_cnpj: str):
        self.client_document = cpf_cnpj.replace('.', '').replace('-', '').replace('/', '')    

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

    def connect(self, url, params={}):
        self.set_headers()
        rq = requests.get(url, headers=self.headers, params=params)
        
        if rq.status_code == 200:
            dados = rq.json()

            return dados
        print(rq.content)
        raise RequestAborted

    @property
    def ativo(self):
        """Conecta à API e verifica se cliente possui compra ativa"""

        active = self.any_sale_active()    

        return active
       

    def any_sale_active(self):
        """
        Verifica se cliente possui alguma compra ativa

        :return: True se possui compra ativa, False caso contrário
        """

        active_in_db = self.select_sale_active_db()
        if active_in_db:
            return True

        else:
            sales = self.sale_list()
            for sale in sales:
                print(sale)
                print('==================')
                
                sale_object, created = Sale.objects.update_or_create(
                    client_document = sale['client_document'],
                    content_id = sale['content_id'],
                    client_email = sale['client_email'],
                    sale_status = sale['sale_status'],
                    defaults={'sale_id': sale['sale_id']}
                )

                if sale_object.sale_status == 3 and sale_object.content_id in self.content_ids:
                    return True
        
        return False
        
    def select_sale_active_db(self):
        """
        Verifica se cliente está cadastrado no banco de dados e está ativo
        
        :return: True se está cadastrado e ativo, False caso contrário
        """

        # busca no banco os cadastros em que o cliente está ativo e não foi atualizado a mais de 1 dia
        sales = Sale.objects.filter(client_document=self.client_document, sale_id__in=self.content_ids, sale_status=3)

        expiration = datetime.now(timezone.utc) - timedelta(days=2)
        for sale in sales:

            # se o cadastro foi atualizado a mais de 1 dia, atualiza o status
            if sale.atualizado_em < expiration:
                sale_data = self.get_sale(sale.sale_id)
                sale.sale_status = sale_data['sale_status']
                sale.save()
                print('sale save')
            
            if sale.sale_status == 3:
                return True

        return False

    def sale_list(self):
        end_date = datetime.now().date()
        start_date = (end_date - timedelta(days=6*30))
        
        params = {
            'client_document': self.client_document,
            'start_date': start_date,
            'end_date': end_date,
        }

        dados = self.connect("https://api2.eduzz.com/sale/get_sale_list", params=params)
        return dados['data']

    def get_sale(self, pk):
        
        dados = self.connect(f"https://api2.eduzz.com/sale/get_sale/{pk}")      
        return dados['data'][-1]



    def get_client(self, pk):
        
        dados = self.connect(f"https://api2.eduzz.com/subscription/{pk}/client")        
        return dados['data'] 
