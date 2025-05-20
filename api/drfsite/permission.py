from rest_framework import permissions


class IsAdminOrAuthForReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_active

        return bool(request.user.is_active and request.user.is_superuser)


class IsAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active


class IsAdminOrAuthForReadOnlyOrCurrentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH'):
            return request.user.is_active
        return bool(request.user.is_active and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_active
        return bool(obj.user == request.user or request.user.is_active and request.user.is_superuser)

