from rest_framework import viewsets
from ..models import City
from ..serializers.city_serializer import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
