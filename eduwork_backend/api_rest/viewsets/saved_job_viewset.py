from rest_framework import viewsets
from ..models import SavedJob
from ..serializers.saved_job_serializer import SavedJobSerializer
from users.permissions import IsStudentUser

class SavedJobViewSet(viewsets.ModelViewSet):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer
    permission_classes = [IsStudentUser]
