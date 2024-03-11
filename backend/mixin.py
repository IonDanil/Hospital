from rest_framework import viewsets



from backend.permissions import RoleBasedPermissionsMixin, HasPermissionByAuthentificatedUserRole

# 12 Урок практика
class HospitalGenericViewSet(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet
):
    permission_classes = [HasPermissionByAuthentificatedUserRole]