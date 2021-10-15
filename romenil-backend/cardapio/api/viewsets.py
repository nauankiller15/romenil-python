from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet


class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):      
        cardapio = 'PNPSNP'  

        return Response({'cardapio': cardapio})

    def create(self, request, *args, **kwargs):
        request.data['usuario'] = request.user.id
        return super().create(request, *args, **kwargs)