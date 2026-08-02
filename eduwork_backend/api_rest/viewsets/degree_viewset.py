from rest_framework import viewsets
from ..models import Degree
from ..serializers.degree_serializer import DegreeSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
