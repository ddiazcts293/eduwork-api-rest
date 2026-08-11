from rest_framework import serializers
from ..models import Interview
from .application_serializer import ApplicationReadSerializer

class InterviewReadSerializer(serializers.ModelSerializer):
    application = ApplicationReadSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = '__all__'
        depth = 1

class InterviewWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'
        read_only_fields = ['id', 'student']

class InterviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'
        read_only_fields = ['id', 'student', 'application']

    def validate_status(self, value):
        if not self.instance:
            return Interview.StatusType.SCHEDULED

        if self.instance.status in [
            Interview.StatusType.COMPLETED,
            Interview.StatusType.CANCELLED,
            Interview.StatusType.NO_SHOW]:
            raise serializers.ValidationError('Cannot change the status of a closed interview')

        return value
