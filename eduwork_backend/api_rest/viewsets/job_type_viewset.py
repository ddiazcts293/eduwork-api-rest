from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import JobType
from ..serializers.job_type_serializer import JobTypeSerializer

class JobTypeViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar los tipos de empleo (tiempo completo, medio tiempo, etc.)
    """
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
