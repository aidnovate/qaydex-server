"""custom permissions for the application."""

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """admin only permission."""

    def has_permission(self, request, view):
        """check if user is admin."""
        from users.choices import UserRoleChoices

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.role == UserRoleChoices.ADMIN
