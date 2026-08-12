from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import Skill
from ..serializers.skill_serializer import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar las habilidades registradas en el sistema.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
