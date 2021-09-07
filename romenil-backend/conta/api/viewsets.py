
from conta.models import Usuario
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import fields, serializers, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

from conta.api.serializers import ContaSerializer, UsuarioSerializer


class ContaViewSet(CreateAPIView, GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = ContaSerializer

  
class UsuarioViewSet(CreateAPIView, GenericViewSet):
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        request.data['usuario'] = request.user.id
        return super().create(request, *args, **kwargs)


class DadosContaViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # self.buscar_dados()
        serializer = ContaSerializer(request.user)
                
        return Response(serializer.data)

class DadosUsuarioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # self.buscar_dados()
        usuario = request.user.usuario_set.last()
        serializer = UsuarioSerializer(usuario)
                
        return Response(serializer.data)
        






    