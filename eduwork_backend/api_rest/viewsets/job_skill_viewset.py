from rest_framework import viewsets
from ..models import JobSkill
from ..serializers.job_skill_serializer import JobSkillSerializer

class JobSkillViewSet(viewsets.ModelViewSet):
    queryset = JobSkill.objects.all()
    serializer_class = JobSkillSerializer
