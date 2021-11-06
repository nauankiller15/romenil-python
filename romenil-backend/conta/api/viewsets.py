
from conta.models import Usuario
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from conta.api.serializers import ContaSerializer, UsuarioSerializer


class ContaViewSet(CreateAPIView, GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [AllowAny]

  
class UsuarioViewSet(CreateAPIView, GenericViewSet):
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['usuario'] = request.user.id
        return super().create(request, *args, **kwargs)


class DadosContaViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ContaSerializer(request.user)
                
        return Response(serializer.data)

class DadosUsuarioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        
        usuario = request.user.usuario_set.last()
        serializer = UsuarioSerializer(usuario)
                
        return Response(serializer.data)
        