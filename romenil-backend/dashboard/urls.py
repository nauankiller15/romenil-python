from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dashboard.api.viewsets import CardapiosViewSet

urlpatterns = [
    path('cardapios/', CardapiosViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
