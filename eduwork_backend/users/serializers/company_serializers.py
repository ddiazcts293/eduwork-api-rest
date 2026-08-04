from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import transaction
from api_rest.models import CompanyProfile
from api_rest.validators import phone_number_validator

User = get_user_model()

class CompanyRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    name = serializers.CharField(write_only=True, max_length=60, required=True)
    sector = serializers.IntegerField(write_only=True, required=True,validators=[MinValueValidator(1)])
    city = serializers.IntegerField(write_only=True, required=True,validators=[MinValueValidator(1)])
    phone_number = serializers.CharField(write_only=True,max_length=20,required=True, validators=[phone_number_validator])

    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'phone_number', 'sector', 'city']

    @transaction.atomic
    def create(self, validated_data):
        email=validated_data.pop('email')
        name = validated_data.pop('name')
        sector = validated_data.pop('sector')
        city = validated_data.pop('city', 1)
        phone_number = validated_data.pop('phone_number')

        user = User.objects.create_user(
            email=email,
            password=validated_data['password'],
            role=User.Role.COMPANY
        )

        company = CompanyProfile.objects.create(
            user=user,
            name=name,
            email_address=email,
            phone_number=phone_number,
            sector_id=sector,
            city_id=city,
        )

        company.save()

        return user
