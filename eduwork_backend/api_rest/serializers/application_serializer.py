from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from ..models import Application
from .job_serializer import JobBasicSerializer
from .student_profile_serializer import StudentProfileBasicSerializer
from users.models import EduWorkUser

class ApplicationReadSerializer(serializers.ModelSerializer):
    job = JobBasicSerializer(read_only=True)
    student = StudentProfileBasicSerializer(read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
        depth = 1

class ApplicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id', 'student', 'status']

    def validate(self, data):
        user = self.context['request'].user
        job = data.get('job')
        print(f'{user}-{job}')

        if hasattr(user, 'student_profile') and job is not None:
            time_limit = timezone.now() - timedelta(days=30)
            recent_application = Application.objects.filter(
                student=user.student_profile,
                job=job,
                created_on__gte=time_limit
            ).exists()

            if recent_application:
                raise serializers.ValidationError({"error": "Cannot apply for the same job within 30 days"})

        return data

class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id', 'student', 'job']

    def validate_status(self, value):
        # Obtiene el usuario actual
        user = self.context['request'].user

        # Ignora el estado si se está creando un registro nuevo
        if not self.instance:
            return Application.StatusType.APPLIED

        # No permite cambios si la postulación actual es contratado, rechazado o retirado
        if self.instance.status in [
            Application.StatusType.HIRED,
            Application.StatusType.REJECTED,
            Application.StatusType.WITHDRAWN]:
            raise serializers.ValidationError('Cannot change the status of a closed application')

        if user.role == EduWorkUser.Role.STUDENT:
            if value != Application.StatusType.WITHDRAWN:
                raise serializers.ValidationError('Students can only change the status to \'Withdrawn\'')
            return value

        if user.role == EduWorkUser.Role.COMPANY:
            if value in [Application.StatusType.WITHDRAWN, Application.StatusType.APPLIED]:
                raise serializers.ValidationError('Invalid status value')
            return value

        return value
