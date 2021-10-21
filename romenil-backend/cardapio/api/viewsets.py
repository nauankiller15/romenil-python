import json
from django.http.response import JsonResponse
from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer, JSONRenderer
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

        if Formulario:
            cardapios = gerar_cardapio(formulario)
            dados = CardapioSerializer(cardapios, many=True).data

        return Response(dados)
