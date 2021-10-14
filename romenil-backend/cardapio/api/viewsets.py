from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from cardapio.api.serializers import PatologiaSerializer

from cardapio.models import Patologia

class CardapioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):      
        cardapio = 'PNPSNP'  

        return Response({'cardapio': cardapio})

    def create(self, request, *args, **kwargs):
        request.data['usuario'] = request.user.id
        return super().create(request, *args, **kwargs)

class PatologiaViewSet(ViewSet):

    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer
    permission_classes = [IsAuthenticated]