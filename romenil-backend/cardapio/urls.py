from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cardapio.api.viewsets import CardapioEmailViewSet, CardapioViewSet

urlpatterns = [
    path('', CardapioViewSet.as_view({'get': 'list'})),
    path('via-email/', CardapioEmailViewSet.as_view({'post': 'post'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
