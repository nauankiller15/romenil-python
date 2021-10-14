from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cardapio.api.viewsets import CardapioViewSet, PatologiaViewSet

urlpatterns = [
    path('', CardapioViewSet.as_view({'get': 'list'})),
    path('patologia/', PatologiaViewSet.as_view({'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
