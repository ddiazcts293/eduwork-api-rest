from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Interview
from ..serializers.interview_serializer import (
    InterviewReadSerializer,
    InterviewWriteSerializer,
    InterviewUpdateSerializer
)
from ..filters import InterviewFilter
from users.permissions import IsCompanyUser, IsInterviewOwner

class InterviewViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las entrevistas agendadas.
    Solo las empresas pueden crear entrevistas y modificarlas
    Tanto empresas como estudiantes pueden consultar sus postulaciones.
    """

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Filtrado exacto
    filterset_class = InterviewFilter
    # Ordenamiento
    ordering_fields = ['registered_on']
    # Ordenamiento por defecto
    ordering = ['-registered_on']

    def get_serializer_class(self):
        if self.action == 'create':
            return InterviewWriteSerializer
        if self.action in ['list', 'retrieve']:
            return InterviewReadSerializer

        return InterviewUpdateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Permite consultar las entrevistas tanto a estudiantes como a empresas
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Permite modificar/eliminar entrevistas solo a empresas
            self.permission_classes = [IsCompanyUser, IsInterviewOwner]
        else:
            # Permite realizar otras acciones a empresas
            self.permission_classes = [IsCompanyUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role'):
            if user.role == 'STUDENT' and hasattr(user, 'student_profile'):
                return Interview.objects.filter(application__student=user.student_profile)\
                    .select_related('application')\
                    .select_related('application__job')\
                    .select_related('application__student')

            if user.role == 'COMPANY' and hasattr(user, 'company_profile'):
                return Interview.objects.filter(application__job__company=user.company_profile)\
                    .select_related('application')\
                    .select_related('application__job')\
                    .select_related('application__student')

            return Interview.objects.all()\
                    .select_related('application')\
                    .select_related('application__job')\
                    .select_related('application__student')

        return Interview.objects.none()
