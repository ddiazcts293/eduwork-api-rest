from rest_framework import viewsets
from ..models import CompanyProfile
from ..serializers.company_profile_serializer import CompanyProfileSerializer

class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'options']
