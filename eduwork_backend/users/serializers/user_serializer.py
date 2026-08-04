from rest_framework import serializers
from ..models import EduWorkUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduWorkUser
        fields = ['email', 'date_joined', 'last_login', 'role']
