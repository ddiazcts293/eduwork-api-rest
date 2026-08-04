from rest_framework import serializers
from ..models import EduWorkUserManager, EduWorkUser

class ChangeEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField(max_length=60, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_new_email(self, value):
        email = EduWorkUserManager.normalize_email(value)
        user = self.context['request'].user

        if email == user.email:
            raise serializers.ValidationError('New email address is the same as the current one')

        if EduWorkUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email address already in use')

        return email

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['password']):
            raise serializers.ValidationError({'password': 'The password is incorrect'})

        return data
