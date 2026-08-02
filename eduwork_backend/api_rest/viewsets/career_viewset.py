from rest_framework import viewsets
from ..models import Career
from ..serializers.career_serializer import CareerSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
