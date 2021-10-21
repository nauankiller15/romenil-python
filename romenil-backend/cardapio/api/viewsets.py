from datetime import datetime, timedelta, timezone

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from cardapio.api.serializers import CardapioSerializer
from cardapio.models import Cardapio

from formulario.models import Formulario

from .cardapio import gerar_cardapio


class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):  

        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        dados = None
        pronto = False

        if Formulario:
            if formulario.modificado_em < datetime.now(timezone.utc) - timedelta(hours=2):
                cardapios = gerar_cardapio(formulario)
                dados = CardapioSerializer(cardapios, many=True).data
                pronto = True

        return Response({'pronto': pronto, 'dados': dados})
