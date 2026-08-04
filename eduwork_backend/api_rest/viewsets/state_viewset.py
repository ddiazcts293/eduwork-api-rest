from rest_framework import viewsets
from ..models import State
from ..serializers.state_serializer import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    http_method_names = ['get', 'head', 'options']
