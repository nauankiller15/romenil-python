from rest_framework.serializers import ModelSerializer

from cardapio.models import Cardapio

class CardapiosSerializer(ModelSerializer):

    class Meta:
        model = Cardapio
        fields = '__all__'