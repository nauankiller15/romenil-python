from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey


from validators.usuario import cpf_or_cnpj_valid


class Usuario(Model):

    usuario = ForeignKey(User, on_delete=CASCADE)
    cpf_ou_cnpj = CharField(max_length=18, unique=True, validators=[cpf_or_cnpj_valid])
    celular = CharField(max_length=15)  

    def is_active(self):
        hoje = timezone.now()
        


class Subscription(Model):

    cpf = CharField(max_length=14, validators=[cpf_or_cnpj_valid])
    contract_status = CharField(max_length=15)  
    contract_cancel_date = CharField(max_length=15) 

