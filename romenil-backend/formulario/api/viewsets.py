from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from formulario.api.serializers import PatologiaSerializer

from formulario.models import Patologia

class PatologiaViewSet(ModelViewSet):

    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.user.id)
        request.data['usuario'] = request.user.usuario_set.last().id
        return super().create(request, *args, **kwargs)
