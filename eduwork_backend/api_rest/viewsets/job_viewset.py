from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import Job
from ..serializers.job_serializer import (
    JobReadSerializer,
    JobWriteSerializer,
    JobBasicSerializer
)
from users.permissions import IsCompanyUser, IsOwnerCompany

class JobViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las ofertas de empleo publicadas.
    Cualquiera puede consultar, pero solo empresas y administradores pueden modificar.
    Las empresas solo pueden consultar sus propias ofertas.
    """

    def get_serializer_class(self):
        if self.action == 'list':
            return JobBasicSerializer
        elif self.action == 'retrieve':
            return JobReadSerializer

        return JobWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Permite consultar las ofertas de empleo a cualquiera
            self.permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Permite modificar a empresas que posean el objeto
            self.permission_classes = [IsCompanyUser, IsOwnerCompany]
        else:
            # Permite realizar otras acciones solo a empresas
            self.permission_classes = [IsCompanyUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role') and user.role == 'COMPANY':
            if hasattr(user, 'company_profile'):
                return Job.objects.filter(company=user.company_profile)\
                    .select_related('company')\
                    .select_related('city')\
                    .select_related('degree')\
                    .select_related('job_type')\
                    .prefetch_related('jobskill_set__skill')

            return Job.objects.none()

        return Job.objects.all()\
            .select_related('company')\
            .select_related('city')\
            .select_related('degree')\
            .select_related('job_type')\
            .prefetch_related('jobskill_set__skill')

    def perform_create(self, serializer):
        # Obtiene el perfil de la empresa directo del usuario que realiza la
        # acción. Esto con el fin de evitar la suplantación de empresas.
        company_profile = self.request.user.company_profile
        serializer.save(company=company_profile)
