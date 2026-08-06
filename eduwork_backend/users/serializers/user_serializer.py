from rest_framework import serializers
from ..models import EduWorkUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduWorkUser
        fields = [
            'email',
            'date_joined',
            'role',
            'student_profile',
            'company_profile',
        ]
        depth = 1
