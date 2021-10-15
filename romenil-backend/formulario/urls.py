from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from formulario.api.viewsets import PatologiaViewSet

urlpatterns = [
    path('patologia/', PatologiaViewSet.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
