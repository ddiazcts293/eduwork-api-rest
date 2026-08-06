from rest_framework.permissions import BasePermission
from .models import EduWorkUser

class IsCompanyUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and # verifica que sea un usuario
            request.user.is_authenticated and # verifica que esté autenticado
            request.user.role in [
                EduWorkUser.Role.COMPANY,
                EduWorkUser.Role.ADMIN
            ] # verifica que el rol sea 'Company' o 'Admin'
        )

class IsStudentUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and # verifica que sea un usuario
            request.user.is_authenticated and # verifica que esté autenticado
            request.user.role in [
                EduWorkUser.Role.STUDENT,
                EduWorkUser.Role.ADMIN
            ] # verifica que el rol sea 'Company' o 'Admin'
        )
