from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from formulario.models import Formulario


class FormularioSerializer(ModelSerializer):

    ativo = SerializerMethodField()

    def get_ativo(self, obj):
        return obj.usuario.ativo

    class Meta:
        model = Formulario        
        fields = '__all__'