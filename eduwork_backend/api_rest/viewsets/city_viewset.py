from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import City
from ..serializers.city_serializer import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
