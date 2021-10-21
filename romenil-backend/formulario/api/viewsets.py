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
        request.data['usuario'] = request.user.usuario_set.last().id
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        usuario = request.user.usuario_set.last()
        formulario = usuario.formulario_set.last()
        dados = None

        if formulario:
            dados = FormularioSerializer(formulario).data
        
        return Response(dados)