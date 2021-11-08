from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from cardapio.models import Cardapio
from dashboard.api.serializers import CardapiosSerializer


class CardapiosViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):  

        cardapios = Cardapio.objects.all()        
        dados = CardapiosSerializer(cardapios, many=True).data

        return Response(dados)
