from rest_framework import serializers
from ..models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        min_salary = data['min_salary']
        max_salary = data['max_salary']

        if min_salary is not None and min_salary <= 0:
            raise serializers.ValidationError({'min_salary': 'Minimum salary cannot be less than or equal to zero'})

        if min_salary and max_salary and min_salary > max_salary:
            raise serializers.ValidationError({'max_salary': 'Maximum salary cannot be less than minimum salary'})

        return data
