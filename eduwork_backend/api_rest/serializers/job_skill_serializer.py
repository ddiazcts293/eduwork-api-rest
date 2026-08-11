from rest_framework import serializers
from ..models import JobSkill
from .skill_serializer import SkillSerializer
from .job_serializer import JobBasicSerializer

class JobSkillReadSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)
    job = JobBasicSerializer(read_only=True)

    class Meta:
        model = JobSkill
        fields = '__all__'

class JobSkillWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = '__all__'
        read_only_fields = ['id']

    def validate_job(self, value):
        user = self.context['request'].user

        if not hasattr(user, 'company_profile') or value.company != user.company_profile:
            raise serializers.ValidationError({
                'error': 'Cannot modify skills associated with jobs that are not owned'
            })

        return value
