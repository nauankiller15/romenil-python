
from conta.models import Usuario
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from conta.api.serializers import AtualizarContaSerializer, MudarSenhaSerializer, ContaSerializer, UsuarioSerializer
from permissions.permissions import OwnerOnly




class ContaViewSet(CreateAPIView, GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [AllowAny]

class AtualizarContaViewSet(UpdateAPIView, GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = AtualizarContaSerializer
    permission_classes = [IsAuthenticated, OwnerOnly]

  
class UsuarioViewSet(CreateAPIView, GenericViewSet):
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
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
        
class MudarSenhaView(UpdateAPIView, GenericViewSet):
        """
        An endpoint for changing password.
        """
        serializer_class = MudarSenhaSerializer
        model = User
        permission_classes = (IsAuthenticated, OwnerOnly)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Senha antiga incorreta."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get

                if serializer.data.get("password1") != serializer.data.get("password2"):
                    return Response({"password2": ["Senhas não conferem."]}, status=status.HTTP_400_BAD_REQUEST)

                self.object.set_password(serializer.data.get("password1"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)