from rest_framework import serializers
from django.utils import timezone
from ..models import Career
from .university_serializer import UniversitySerializer

class CareerReadSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Career
        exclude = ['student']
        depth = 2

class CareerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        read_only_fields = ['id', 'student']

    def validate(self, data):
        starting_date = data.get('starting_date')
        finishing_date = data.get('finishing_date')

        if starting_date is not None and starting_date > timezone.now().date():
            raise serializers.ValidationError({'starting_date': 'Starting date cannot be later than the current date'})

        if finishing_date is not None and starting_date >= finishing_date:
            raise serializers.ValidationError({'finishing_date': 'Finishing date cannot be equal to or earlier than the starting date'})

        return data
