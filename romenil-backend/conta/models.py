from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey
from coneccao_APIs.models import Eduzz


from validators.usuario import cpf_or_cnpj_valid


class Usuario(Model):

    user = ForeignKey(User, on_delete=CASCADE)
    cpf_ou_cnpj = CharField(max_length=18, unique=True, validators=[cpf_or_cnpj_valid])
    celular = CharField(max_length=15)  

    @property
    def ativo(self):

        produto_ativo = False

        if self.cpf_ou_cnpj:
            eduzz = Eduzz(self.cpf_ou_cnpj)
            produto_ativo = eduzz.ativo

        administracao = False
        if self.user.is_staff:
            administracao = True
        else:
            cargos = self.user.cargo_set.all()
            for cargo in cargos:
                if cargo.cargo in ['desenvolvedor', 'administrador']:
                    administracao = True
                    break

        return produto_ativo or administracao

    def data_formulario(self):
        patologia = self.patologia_set.last()

        return patologia.modificado_em

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.cpf_ou_cnpj}'
    