from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import University
from ..serializers.university_serializer import UniversitySerializer

class UniversityViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las universidades registradas en la plataforma.
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
