from rest_framework import serializers
from ..models import StudentProfile
from ..validators import NameValidator, AgeValidator, phone_number_validator

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        read_only_fields = ['id']

    first_name = serializers.CharField(max_length=60, validators=[NameValidator()])
    last_name = serializers.CharField(max_length=60, validators=[NameValidator()])
    date_of_birth = serializers.DateField(validators=[AgeValidator()])
    phone_number = serializers.CharField(max_length=20, validators=[phone_number_validator])
