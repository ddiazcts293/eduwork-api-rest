from rest_framework import viewsets
from ..models import Interview
from ..serializers.interview_serializer import InterviewSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
