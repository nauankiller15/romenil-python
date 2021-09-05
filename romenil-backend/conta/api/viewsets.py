
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import fields, serializers
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

from conta.api.serializers import UserSerializer


class UsuarioViewSet(CreateAPIView, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DadosUsuarioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        self.buscar_dados()
        # serializer = UserSerializer(request.user)
        # data = serializer.data
        
        return Response(status=200)
        






    