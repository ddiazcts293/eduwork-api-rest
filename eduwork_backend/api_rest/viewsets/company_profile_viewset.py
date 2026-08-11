from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsCompanyUser, IsOwnerProfile
from ..models import CompanyProfile
from ..serializers.company_profile_serializer import (
    CompanyProfileBasicSerializer,
    CompanyProfileReadSerializer,
    CompanyProfileWriteSerializer
)

class CompanyProfileViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las empresas registradas.
    Cualquiera puede consultar, pero solo los propietarios pueden modificar.
    """

    queryset = CompanyProfile.objects.all()
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

    def get_serializer_class(self):
        if self.action == 'list':
            return CompanyProfileBasicSerializer
        if self.action == 'retrieve':
            return CompanyProfileReadSerializer

        return CompanyProfileWriteSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsCompanyUser, IsOwnerProfile]
        else:
            self.permission_classes = [IsCompanyUser]

        return [permission() for permission in self.permission_classes]
