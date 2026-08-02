from rest_framework import viewsets
from ..models import Application
from ..serializers.application_serializer import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
