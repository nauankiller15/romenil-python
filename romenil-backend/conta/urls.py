from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_jwt.views import ObtainJSONWebToken

from conta.api.serializers import CustomJWTSerializer
from conta.api.viewsets import AtualizarContaViewSet, ContaViewSet, DadosContaViewSet, DadosUsuarioViewSet, MudarSenhaView, UsuarioViewSet

urlpatterns = [
    path('dados/', DadosContaViewSet.as_view({'get': 'list'})),
    path('usuario/', DadosUsuarioViewSet.as_view({'get': 'list'})),
    path('atualizar/<int:pk>/', AtualizarContaViewSet.as_view({'put': 'update'})),
    path('mudar-senha/<int:pk>/', MudarSenhaView.as_view({'put': 'update'})),
    path('criar-conta/', ContaViewSet.as_view({'post': 'create'})),
    path('criar-usuario/', UsuarioViewSet.as_view({'post': 'create'})),
    path('login/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
