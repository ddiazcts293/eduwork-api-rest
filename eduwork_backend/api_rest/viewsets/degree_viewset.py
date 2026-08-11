from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import Degree
from ..serializers.degree_serializer import DegreeSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
