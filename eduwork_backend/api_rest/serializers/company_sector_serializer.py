from rest_framework import serializers
from ..models import CompanySector

class CompanySectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySector
        fields = '__all__'
        read_only_fields = ['id']
