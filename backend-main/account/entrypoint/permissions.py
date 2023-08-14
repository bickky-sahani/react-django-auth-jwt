from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET request for the list action only to superusers (staff).
        if view.action == "list":
            return request.user.is_staff or request.user.is_superuser
        # Allow DELETE request for the delete action only to superusers (staff).
        elif view.action == "delete":
            return request.user.is_staff or request.user.is_superuser
        return True  # Allow other actions for all users.
