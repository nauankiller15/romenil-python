from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from formulario.models import Patologia

from .cardapio import gerar_cardapio


class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):  

        usuario = request.user.usuario_set.last()
        patologia = usuario.patologia_set.last()
        cardapio = gerar_cardapio(patologia)

        return Response({'cardapio': cardapio})
