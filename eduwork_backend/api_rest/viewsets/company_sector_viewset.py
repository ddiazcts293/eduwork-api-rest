from rest_framework import viewsets
from ..models import CompanySector
from ..serializers.company_sector_serializer import CompanySectorSerializer

class CompanySectorViewSet(viewsets.ModelViewSet):
    queryset = CompanySector.objects.all()
    serializer_class = CompanySectorSerializer
    http_method_names = ['get', 'head', 'options']
