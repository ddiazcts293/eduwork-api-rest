from rest_framework import serializers
from ..models import JobSkill

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = '__all__'
        read_only_fields = ['id']
