from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import DateField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models.fields import DateTimeField

from conta.models import Usuario

class Patologia(Model):

    data = DateField(auto_now_add=True)
    usuario = ForeignKey(Usuario, on_delete=CASCADE)

    hipertensao = BooleanField()
    diabetes = BooleanField()
    metabolismo_lento = BooleanField()
    constipacao = BooleanField()
    insonia = BooleanField()
    colesterol_elevado = BooleanField()
    ansiedade = BooleanField()
    retencao_liquida = BooleanField()
    hipotireoidismo = BooleanField()
    gordura_no_figado = BooleanField()
    anemia = BooleanField()
    modificado_em = DateTimeField(auto_now=True)

class Alergia(Model):

    data = DateField(auto_now_add=True)
    usuario = ForeignKey(Usuario, on_delete=CASCADE)

    lactose = BooleanField()
    frutos_do_mar = BooleanField()
    ovo = BooleanField()
    soja = BooleanField()
    amendoim = BooleanField()
   
class EstiloDeVida(Model):

    data = DateField(auto_now_add=True)
    usuario = ForeignKey(Usuario, on_delete=CASCADE)

    vegano = BooleanField()
    vegetariano = BooleanField()