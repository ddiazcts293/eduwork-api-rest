from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Career
from ..serializers.career_serializer import (
    CareerReadSerializer,
    CareerWriteSerializer
)
from ..filters import CareerFilter
from users.permissions import IsStudentUser, IsOwnerStudent

class CareerViewSet(viewsets.ModelViewSet):

    # Motores de filtrado
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Filtrado exacto
    filterset_class = CareerFilter
    # Ordenamiento
    ordering_fields = ['starting_date', 'finishing_date']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CareerReadSerializer

        return CareerWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Permite consultar la información de carreras a usuarios autenticados
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            # Permite crear carreras a estudiantes
            self.permission_classes = [IsStudentUser]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Permite eliminar carreras solo a estudiantes
            self.permission_classes = [IsStudentUser, IsOwnerStudent]
        else:
            # Permite realizar otras acciones a empresas y estudiantes
            self.permission_classes = [IsStudentUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'role'):
            if user.role == 'STUDENT' and hasattr(user, 'student_profile'):
                return Career.objects.filter(student=user.student_profile)\
                    .select_related('university')\
                    .select_related('university__city')\
                    .select_related('degree')

            return Career.objects.all()\
                    .select_related('university')\
                    .select_related('university__city')\
                    .select_related('degree')

        return Career.objects.none()

    def perform_create(self, serializer):
        student_profile = self.request.user.student_profile
        serializer.save(student=student_profile)
