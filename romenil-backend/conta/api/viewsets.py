
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import fields, serializers, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

from conta.api.serializers import UserSerializer, UsuarioSerializer


class UsuarioViewSet(CreateAPIView, GenericViewSet):
    
    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        usuario_serializer = UsuarioSerializer(data=request.data)

        user_serializer.is_valid(raise_exception=True)
        usuario_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()
        print(user)
        usuario = usuario_serializer.save(commit=False)
        print(usuario)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


class DadosUsuarioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        self.buscar_dados()
        # serializer = UserSerializer(request.user)
        # data = serializer.data
        
        return Response(status=200)
        






    