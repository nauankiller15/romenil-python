from rest_framework.serializers import ModelSerializer

from formulario.models import Patologia


class PatologiaSerializer(ModelSerializer):

    class Meta:
        model = Patologia        
        fields = '__all__'