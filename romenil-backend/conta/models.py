import re
from django.db.models.fields import DateField, EmailField, IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey
from coneccao_APIs.models import Eduzz


from validators.usuario import cpf_or_cnpj_valid


class Usuario(Model):

    usuario = ForeignKey(User, on_delete=CASCADE)
    cpf_ou_cnpj = CharField(max_length=18, unique=True, validators=[cpf_or_cnpj_valid])
    celular = CharField(max_length=15)  

    def ativo(self):
        eduzz = Eduzz(self.cpf_ou_cnpj)
        produto_ativo = eduzz.ativo
        return produto_ativo

    def data_formulario(self):
        patologia = self.patologia_set.last()

        return patologia.modificado_em