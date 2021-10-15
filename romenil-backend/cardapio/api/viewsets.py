from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from formulario.models import Patologia

from .cardapio import gerar_cardapio


class CardapioViewSet(ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def list(self, request):  
        template_name='cardapio/teste.html'

        usuario = request.user.usuario_set.last()
        patologia = usuario.patologia_set.last()

        if patologia:
            cardapio = gerar_cardapio(patologia)
            template_name = f'cardapio/{cardapio}.html'

        return Response(template_name=template_name, content_type='text/html')
