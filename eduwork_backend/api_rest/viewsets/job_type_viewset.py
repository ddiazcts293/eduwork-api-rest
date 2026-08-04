from rest_framework import viewsets
from ..models import JobType
from ..serializers.job_type_serializer import JobTypeSerializer

class JobTypeViewSet(viewsets.ModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    http_method_names = ['get', 'head', 'options']
