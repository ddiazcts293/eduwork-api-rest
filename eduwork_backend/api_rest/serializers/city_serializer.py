from rest_framework import serializers
from ..models import City

class CitySerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.name', read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'state_name']
        read_only_fields = ['id']
