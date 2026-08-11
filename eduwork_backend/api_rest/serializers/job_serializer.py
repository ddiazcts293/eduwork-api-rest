from rest_framework import serializers
from ..models import Job
from .city_serializer import CitySerializer
from .company_profile_serializer import CompanyProfileBasicSerializer

class JobReadSerializer(serializers.ModelSerializer):
    company = CompanyProfileBasicSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        depth = 1

class JobWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id', 'company']

    def validate(self, data):
        min_salary = data.get('min_salary')
        max_salary = data.get('max_salary')

        if min_salary is not None and min_salary <= 0:
            raise serializers.ValidationError({'min_salary': 'Minimum salary cannot be less than or equal to zero'})

        if min_salary is not None and max_salary is not None and max_salary <= min_salary:
            raise serializers.ValidationError({'max_salary': 'Maximum salary cannot be less than minimum salary'})

        return data
