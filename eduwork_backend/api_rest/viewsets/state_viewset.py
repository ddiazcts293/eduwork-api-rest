from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import State
from ..serializers.state_serializer import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head', 'options']
