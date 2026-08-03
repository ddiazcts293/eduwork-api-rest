from rest_framework import serializers
from ..models import Career
from django.utils import timezone

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        starting_date = data['starting_date']
        finishing_date = data['finishing_date']

        if starting_date is not None and starting_date > timezone.now().date():
            raise serializers.ValidationError({'starting_date': 'Starting date cannot be later than the current date'})

        if starting_date and finishing_date and starting_date > finishing_date:
            raise serializers.ValidationError({'finishing_date': 'Finishing date cannot be earlier than the starting date'})

        return data
