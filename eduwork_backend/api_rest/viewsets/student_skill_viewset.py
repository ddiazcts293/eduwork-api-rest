from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from ..models import StudentSkill
from ..serializers.student_skill_serializer import (
    StudentSkillReadSerializer,
    StudentSkillWriteSerializer
)
from ..filters import StudentSkillFilter
from users.permissions import IsStudentUser, IsOwnerStudent

class StudentSkillViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las habilidades asociadas a las estudiantes.
    """
    queryset = StudentSkill.objects.all()
    http_method_names = ['get', 'post', 'delete']

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend]
    # Filtrado exacto
    filterset_class = StudentSkillFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return StudentSkillReadSerializer

        return StudentSkillWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsStudentUser, IsOwnerStudent]
        else:
            self.permission_classes = [IsStudentUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role'):
            if user.role == 'STUDENT' and hasattr(user, 'student_profile'):
                return StudentSkill.objects.filter(student=user.student_profile)\
                    .select_related('student')\
                    .select_related('skill')

            return StudentSkill.objects.all()\
                .select_related('student')\
                .select_related('skill')

        return StudentSkill.objects.none()

    def perform_create(self, serializer):
        student_profile = self.request.user.student_profile
        serializer.save(student=student_profile)
