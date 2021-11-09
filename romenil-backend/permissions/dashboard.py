from rest_framework.permissions import BasePermission


class Desenvolvedor(BasePermission):
    """
    A requisição deve ser feita por um desenvolvedor.
    """

    def has_permission(self, request, view):
        
        cargo = request.user.cargo_set.last()
            
        if (cargo and cargo.perfil.lower == 'desenvolvedor') or request.user.is_staff:
            return True
           
        return False
        
