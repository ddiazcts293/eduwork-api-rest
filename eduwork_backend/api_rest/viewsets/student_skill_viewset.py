from rest_framework import viewsets
from ..models import StudentSkill
from ..serializers.student_skill_serializer import StudentSkillSerializer

class StudentSkillViewSet(viewsets.ModelViewSet):
    queryset = StudentSkill.objects.all()
    serializer_class = StudentSkillSerializer
