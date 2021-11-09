from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import DateField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models.fields import DateTimeField

from conta.models import Usuario

class Formulario(Model):

    usuario = ForeignKey(Usuario, on_delete=CASCADE)

    hipertensao = BooleanField()
    diabetes = BooleanField()
    celiaco = BooleanField()
    metabolismo_lento = BooleanField()
    constipacao = BooleanField()
    insonia = BooleanField()
    colesterol_elevado = BooleanField()
    ansiedade = BooleanField()
    retencao_liquida = BooleanField()
    hipotireoidismo = BooleanField()
    gordura_no_figado = BooleanField()
    anemia = BooleanField()

    # Alergia
    frutos_do_mar = BooleanField()
    ovo = BooleanField()
    soja = BooleanField()
    amendoim = BooleanField()
   
    # EstiloDeVida
    vegano = BooleanField()
    vegetariano = BooleanField()
    
    modificado_em = DateTimeField(auto_now=True)