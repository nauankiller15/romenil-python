from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from formulario.models import Formulario


class FormularioSerializer(ModelSerializer):

    class Meta:
        model = Formulario        
        fields = '__all__'