from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils import timezone
from ..models import CompanyProfile
from ..validators import phone_number_validator
from .city_serializer import CitySerializer

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

class CompanyProfileReadSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = CompanyProfile
        exclude = ['user']
        read_only_fields = ['id']
        depth = 1

class CompanyProfileWriteSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(queryset=CompanyProfile.objects.all())
        ]
    )
    email_address = serializers.EmailField(
        max_length=60,
        validators=[
            UniqueValidator(queryset=CompanyProfile.objects.all())
        ]
    )

    class Meta:
        model = CompanyProfile
        read_only_fields = ['id', 'user']
        exclude = ['user']

    def validate_establish_year(self, value):
        if value > timezone.now().date().year or value < 578:
            raise serializers.ValidationError('Enter a valid year')
        return value
