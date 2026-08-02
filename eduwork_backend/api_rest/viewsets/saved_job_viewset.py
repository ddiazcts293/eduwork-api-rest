from rest_framework import viewsets
from ..models import SavedJob
from ..serializers.saved_job_serializer import SavedJobSerializer

class SavedJobViewSet(viewsets.ModelViewSet):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer
