from django.contrib.auth.models import Permission
from rest_framework import permissions


class DoctorAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return 'backend.view_doctor' in request.user.get_user_permissions()

# 12 Урок практика
class RoleBasedPermissionsMixin:
    """
    Role based permissions for authorization system - Ролевые разрешения для системы авторизации
    """
    # You'll need to either set these attributes, - Вам нужно будет либо установить эти атрибуты,
    # or override 'get_action_permissions()' - или переопределить 'get_action_permissions()'
    action_permissions = None

    def get_action_permissions(self):
        """
        Match the list of permissions that this view requires. - Сопоставьте список разрешений, которые требуются для этого представления.
        You can specify permissions for each action by overriding method - Вы можете указать разрешения для каждого действия, переопределив метод.
        """
        self.action_permissions = None

    def get_permissions(self):
        self.get_action_permissions() # Get role based permissions - Получите разрешения на основе ролей
        assert isinstance(self.action_permissions, list), (
                'Expected a `List` type of self.action_permissions '
                'but received a `%s`'
                % type(self.action_permissions)
        )
        return super().get_permissions() # Overriding existing method of APIView - Переопределение существующего метода APIView


class HasPermissionByAuthentificatedUserRole(permissions.BasePermission):
    """
    Role based access - Ролевой доступ
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if len(view.action_permissions) == 0:
                return True
            for permissions in view.action_permissions:
                if has_perm(permissions, request.user):
                    return True
        return False


def has_perm(perm, user):
    print(get_user_permissons(user))
    return user.is_active and perm in get_user_permissons(user)
def get_user_permissons(user):
    if user.is_superuser:
        return Permission.objects.values_list('codename', flat=True)

    return user.user_permissions.values_list('codename', flat=True) | Permission.objects.filter(
        group__user=user).values_list('codename', flat=True)