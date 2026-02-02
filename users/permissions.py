from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Проверяет, является ли пользователь модератором
    """

    message = "Adding course or lessons not allowed."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модераторы").exists()


class IsOwner(BasePermission):
    """
    Проверяет, является ли пользователь владельцем
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
