from rest_framework.permissions import BasePermission


class IsAuthenticatedOrCreateOnly(BasePermission):

    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated) or request.method == 'POST')
