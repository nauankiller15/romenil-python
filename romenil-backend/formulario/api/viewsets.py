from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from formulario.api.serializers import FormularioSerializer

from formulario.models import Formulario

class FormularioViewSet(ModelViewSet):

    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        if formulario:
            serializer = self.get_serializer(formulario, data=request.data)
        else:
            request.data['usuario'] = usuario.id
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        dados = None

        if formulario:
            dados = FormularioSerializer(formulario).data
        
        return Response(dados)