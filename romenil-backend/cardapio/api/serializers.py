from rest_framework.serializers import ModelSerializer

from cardapio.models import Patologia

class PatologiaSerializer(ModelSerializer):

    class Meta:
        model = Patologia        
        fields = '__all__'