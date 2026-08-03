from rest_framework import serializers
from django.core.validators import RegexValidator
from ..models import CompanyProfile
from django.utils import timezone

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
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

    def validate_establish_year(self, value):
        if value > timezone.now().date().year or value < 578:
            raise serializers.ValidationError('Enter a valid year')
        return value
