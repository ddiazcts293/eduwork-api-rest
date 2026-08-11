from rest_framework import serializers
from ..models import CompanyProfile
from django.utils import timezone
from ..validators import phone_number_validator

class CompanyProfileBasicSerializer(serializers.ModelSerializer):
    sector_description = serializers.CharField(source='sector.description', read_only=True)

    class Meta:
        model = CompanyProfile
        fields = [
            'id',
            'name',
            'website',
            'email_address',
            'sector_description',
        ]

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        exclude = ['user']
        read_only_fields = ['id']

    phone_number = serializers.CharField(max_length=20, validators=[phone_number_validator])

    def validate_establish_year(self, value):
        if value > timezone.now().date().year or value < 578:
            raise serializers.ValidationError('Enter a valid year')
        return value
