from rest_framework import permissions

class AuthServicePermission(permissions.BasePermission):
    """
    Custom authentication Header, API will not respond without this Header.
    """

    def has_permission(self, request, view):
        custom_header = request.META.get('HTTP_X_HEADER')
        return custom_header == 'product-service'
