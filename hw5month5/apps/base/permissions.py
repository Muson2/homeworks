from rest_framework.permissions import BasePermission

class CreateOnlyAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        return True
