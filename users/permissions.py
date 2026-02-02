from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Adding course or lessons not allowed."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модераторы").exists()

