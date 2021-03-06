"""Set permissions for users."""

from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """Object-level permission to only allow owners of an object to edit it."""

    def has_permission(self, request, view):
        """Check if user has required permissions."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Check if user has required permissions."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
