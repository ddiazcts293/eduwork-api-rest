from rest_framework import serializers
from django.core.validators import RegexValidator
from ..models import StudentProfile
from ..validators.model_validators import is_name_valid
from django.utils import timezone

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        read_only_fields = ['id']

    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^(\+?\d{1,3}-)?\d{3}-\d{3}-\d{4}$',
                message="Enter a valid phone number"
            )
        ]
    )

    def validate_first_name(self, value):
        if not is_name_valid(value):
            raise serializers.ValidationError('Last name cannot contain numbers')
        return value.title()

    def validate_last_name(self, value):
        if not is_name_valid(value):
            raise serializers.ValidationError('Last name cannot contain numbers')
        return value.title()

    def validate_date_of_birth(self, value):
        today = timezone.now().date()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError('Must be 18 years old in order to create an student account')
        elif age > 120:
            raise serializers.ValidationError('Enter a valid date')
        return value
