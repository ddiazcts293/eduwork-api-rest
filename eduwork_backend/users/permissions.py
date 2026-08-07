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

class IsOwnerStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite consultar por cualquier usuario
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Verifica si el objeto tiene una referencia al perfil de estudiante
        if not hasattr(request.user, 'student_profile'):
            return False

        # Verifica si el perfil de la empresa coincide con el del usuario
        return obj.student == request.user.student_profile

class IsOwnerCompany(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite consultar por cualquier usuario
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Verifica si el objeto tiene una referencia al perfil de la empresa
        if not hasattr(request.user, 'company_profile'):
            return False

        # Verifica si el perfil de la empresa coincide con el del usuario
        return obj.company == request.user.company_profile

class IsOwnerProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite consultar por cualquier usuario
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Verifica si el usuario del perfil coincide con el del usuario
        return obj.user == request.user
