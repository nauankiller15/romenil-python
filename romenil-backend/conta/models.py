from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey


from validators.usuario import cpf_or_cnpj_valid


class Usuario(Model):

    PLATAFORMAS = {('hotmart', 'hotmart'), ('eduzz', 'eduzz')}

    usuario = ForeignKey(User, on_delete=CASCADE)
    cpf_ou_cnpj = CharField(max_length=18, validators=[cpf_or_cnpj_valid])
    celular = CharField(max_length=14)  
    plataforma = CharField(max_length=14, choices=PLATAFORMAS)  

    def is_active(self):
        hoje = timezone.now()
        


class Subscription(Model):

    PLATAFORMAS = {('hotmart', 'hotmart'), ('eduzz', 'eduzz')}

    cpf = CharField(max_length=14, validators=[cpf_or_cnpj_valid])
    plataforma = CharField(max_length=14, choices=PLATAFORMAS)  
    contract_status = CharField(max_length=15)  
    contract_cancel_date = CharField(max_length=15) 

