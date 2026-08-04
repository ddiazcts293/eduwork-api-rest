from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import transaction
from api_rest.models import StudentProfile
from api_rest.validators import phone_number_validator, AgeValidator, NameValidator

User = get_user_model()

class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    first_name = serializers.CharField(write_only=True, max_length=60, required=True, validators=[NameValidator()])
    last_name = serializers.CharField(write_only=True, max_length=60, required=True, validators=[NameValidator()])
    date_of_birth = serializers.DateField(write_only=True, required=True, validators=[AgeValidator()])
    city = serializers.IntegerField(write_only=True, required=True, validators=[MinValueValidator(1)])
    phone_number = serializers.CharField(write_only=True, max_length=20, required=True, validators=[phone_number_validator])

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'city'
        ]

    @transaction.atomic
    def create(self, validated_data):
        email=validated_data.pop('email')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        date_of_birth = validated_data.pop('date_of_birth')
        city = validated_data.pop('city', 1)
        phone_number = validated_data.pop('phone_number')

        user = User.objects.create_user(
            email=email,
            password=validated_data['password'],
            role=User.Role.STUDENT
        )

        student = StudentProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email_address=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            city_id=city,
        )

        student.save()

        return user
