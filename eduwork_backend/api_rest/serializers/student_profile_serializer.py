from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import StudentProfile
from ..validators import NameValidator, AgeValidator, phone_number_validator
from .city_serializer import CitySerializer

class StudentProfileBasicSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model = StudentProfile
        fields = [
            'id',
            'full_name',
            'email_address',
            'phone_number',
            'date_of_birth',
            'city_name'
        ]

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

class StudentProfileReadSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = StudentProfile
        exclude = ['user']
        read_only_fields = ['id']
        depth = 1

class StudentProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ['user', 'skills']
        read_only_fields = ['id', 'user']

    first_name = serializers.CharField(max_length=60, validators=[NameValidator()])
    last_name = serializers.CharField(max_length=60, validators=[NameValidator()])
    date_of_birth = serializers.DateField(validators=[AgeValidator()])
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(queryset=StudentProfile.objects.all())
        ]
    )
    email_address = serializers.EmailField(
        max_length=60,
        validators=[
            UniqueValidator(queryset=StudentProfile.objects.all())
        ]
    )
