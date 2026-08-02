from rest_framework import viewsets
from ..models import Job
from ..serializers.job_serializer import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
