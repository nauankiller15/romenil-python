from validators.usuario import cpf_is_valid
from django.db.models import CASCADE
from django.db.models import Model
from django.db.models import ForeignKey
from django.contrib.auth.models import User
from django.db.models import CharField

class Usuario(Model):
    TEMA_CHOICES = {('default', 'default'), ('dark', 'dark')}

    usuario = ForeignKey(User, on_delete=CASCADE)
    tema = CharField(max_length=7, choices=TEMA_CHOICES)
    cpf = CharField(max_length=14, validators=cpf_is_valid)
