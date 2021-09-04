from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from conta.api.viewsets import DadosUsuarioViewSet

urlpatterns = [
    path('conta/', DadosUsuarioViewSet.as_view({'get': 'list'})),

]

urlpatterns = format_suffix_patterns(urlpatterns)
