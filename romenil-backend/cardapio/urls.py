from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cardapio.api.viewsets import CardapioViewSet

urlpatterns = [
    path('', CardapioViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
