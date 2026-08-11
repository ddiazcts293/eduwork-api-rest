from rest_framework import serializers
from ..models import StudentSkill
from .skill_serializer import SkillSerializer
from .student_profile_serializer import StudentProfileBasicSerializer

class StudentSkillReadSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)
    student = StudentProfileBasicSerializer(read_only=True)

    class Meta:
        model = StudentSkill
        fields = '__all__'

class StudentSkillWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSkill
        fields = '__all__'
        read_only_fields = ['id', 'student']
