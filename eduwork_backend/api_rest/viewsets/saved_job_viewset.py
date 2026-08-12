from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import SavedJob
from ..serializers.saved_job_serializer import SavedJobWriteSerializer, SavedJobReadSerializer
from ..filters import SavedJobFilter
from users.permissions import IsStudentUser, IsOwnerStudent

class SavedJobViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar los empleos guardados por los estudiantes.
    Solo los estudiantes pueden acceder.
    """
    http_method_names = ['get', 'post', 'delete']

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend]
    # Filtrado exacto
    filterset_class = SavedJobFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SavedJobReadSerializer

        return SavedJobWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsStudentUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsStudentUser, IsOwnerStudent]
        else:
            self.permission_classes = [IsStudentUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role') and user.role == 'STUDENT':
            if hasattr(user, 'student_profile'):
                return SavedJob.objects.filter(student=user.student_profile)

        return SavedJob.objects.none()

    def perform_create(self, serializer):
        student_profile = self.request.user.student_profile
        serializer.save(student=student_profile)
