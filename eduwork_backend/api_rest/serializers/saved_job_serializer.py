from rest_framework import serializers
from ..models import SavedJob
from .job_serializer import JobReadSerializer

class SavedJobReadSerializer(serializers.ModelSerializer):
    job = JobReadSerializer(read_only=True)

    class Meta:
        model = SavedJob
        fields = ['id', 'job', 'saved_on']
        depth = 2

class SavedJobWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = '__all__'
        read_only_fields = ['id', 'student']
