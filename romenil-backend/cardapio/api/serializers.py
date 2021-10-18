from rest_framework.serializers import ModelSerializer

from cardapio.models import Cardapio

class CardapioSerializer(ModelSerializer):

    class Meta:
        model = Cardapio
        fields = ['refeicao', 'prato']