from rest_framework.permissions import BasePermission

from apps.users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.ADMIN


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.USER
