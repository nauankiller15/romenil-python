from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from permissoes.api.viewsets import CargoViewSet

urlpatterns = [
    path('listar/', CargoViewSet.as_view({'get': 'list'})),
    path('criar/', CargoViewSet.as_view({'post': 'create'})),
    path('selecionar/<int:pk>/', CargoViewSet.as_view({'get': 'retrieve'})),
    path('editar/<int:pk>/', CargoViewSet.as_view({'put': 'update'})),
    path('excluir/<int:pk>/', CargoViewSet.as_view({'delete': 'destroy'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
