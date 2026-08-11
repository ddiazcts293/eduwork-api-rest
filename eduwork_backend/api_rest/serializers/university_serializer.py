from rest_framework import serializers
from ..models import University
from .city_serializer import CitySerializer

class UniversitySerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = University
        fields = '__all__'
        read_only_fields = ['id']
        depth=2
