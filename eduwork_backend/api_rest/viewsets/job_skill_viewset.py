from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..models import JobSkill
from ..serializers.job_skill_serializer import (
    JobSkillReadSerializer,
    JobSkillWriteSerializer
)
from ..filters import JobSkillFilter
from users.permissions import IsCompanyUser, IsJobSkillOwner

class JobSkillViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las habilidades asociadas a las vacantes.
    """
    queryset = JobSkill.objects.all()
    http_method_names = ['get', 'post', 'delete']

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend]
    # Filtrado exacto
    filterset_class = JobSkillFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return JobSkillReadSerializer

        return JobSkillWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsCompanyUser, IsJobSkillOwner]
        else:
            self.permission_classes = [IsCompanyUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role') and user.role == 'COMPANY' and hasattr(user, 'company_profile'):
            return JobSkill.objects.filter(job__company=user.company_profile)\
                .select_related('job')\
                .select_related('skill')

        return JobSkill.objects.all()\
            .select_related('job')\
            .select_related('skill')
