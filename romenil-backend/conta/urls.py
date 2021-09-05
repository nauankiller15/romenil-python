from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_jwt.views import ObtainJSONWebToken

from conta.api.serializers import CustomJWTSerializer
from conta.api.viewsets import DadosUsuarioViewSet, UsuarioViewSet

urlpatterns = [
    path('', DadosUsuarioViewSet.as_view({'get': 'list'})),
    path('create', UsuarioViewSet.as_view({'post': 'create'})),
    path('login/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
