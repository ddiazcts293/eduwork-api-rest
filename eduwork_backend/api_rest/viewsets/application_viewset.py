from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Application
from ..serializers.application_serializer import (
    ApplicationWriteSerializer,
    ApplicationReadSerializer,
    ApplicationUpdateSerializer
)
from users.permissions import IsStudentUser, IsOwnerStudent

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las postulaciones que los estudiantes realizan a un empleo.
    Solo los estudiantes pueden crear postulaciones, cambiar su estado a 'Retirado' y eliminarlas.
    Solo las empresas pueden cambiar el estado de una postulación.
    Tanto empresas como estudiantes pueden consultar y modificar sus postulaciones.
    """

    def get_serializer_class(self):
        if self.action == 'create':
            return ApplicationWriteSerializer

        if self.action in ['list', 'retrieve']:
            return ApplicationReadSerializer

        return ApplicationUpdateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update']:
            # Permite consultar y modificar las postulaciones tanto a estudiantes como a empresas
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            # Permite crear postulaciones a estudiantes
            self.permission_classes = [IsStudentUser]
        elif self.action in ['destroy']:
            # Permite eliminar postulaciones solo a estudiantes
            self.permission_classes = [IsStudentUser, IsOwnerStudent]
        else:
            # Permite realizar otras acciones a empresas y estudiantes
            self.permission_classes = [IsAuthenticated]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role'):
            if user.role == 'STUDENT' and hasattr(user, 'student_profile'):
                return Application.objects.filter(student=user.student_profile)

            if user.role == 'COMPANY' and hasattr(user, 'company_profile'):
                return Application.objects.filter(job__company=user.company_profile)

            return Application.objects.all()

        return Application.objects.none()

    def perform_create(self, serializer):
        student_profile = self.request.user.student_profile
        serializer.save(student=student_profile, status=Application.StatusType.APPLIED)
