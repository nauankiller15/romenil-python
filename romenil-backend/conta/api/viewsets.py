from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from conta.api.serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet, ViewSet


class UsuarioViewSet(ListCreateAPIView, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DadosUsuarioViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        self.buscar_dados()
        # serializer = UserSerializer(request.user)
        # data = serializer.data
        
        return Response(status=200)
        


    