from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from permissions.dashboard import Desenvolvedor

from permissoes.api.serializers import CargoSerializer
from permissoes.models import Cargo


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated, Desenvolvedor]
