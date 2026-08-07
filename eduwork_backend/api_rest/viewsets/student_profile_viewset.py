from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import StudentProfile
from ..serializers.student_profile_serializer import StudentProfileSerializer
from users.permissions import IsCompanyUser, IsStudentUser, IsOwnerProfile
from users.models import EduWorkUser

class StudentProfileViewSet(viewsets.ModelViewSet):
    """
    Apartado para consultar los perfiles de los estudiantes.
    Solo las empresas pueden consultar todo el listado de estudiantes.
    Solo los estudiantes pueden modificar su información
    """
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

    def get_permissions(self):
        if self.action == 'list':
            # Permite consultar los perfiles de estudiantes solo a las empresas
            self.permission_classes = [IsCompanyUser]
        elif self.action == 'retrieve':
            # Permite consultar un perfil específico a usuarios autenticados
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            # Permite modificar perfiles solo a estudiantes
            self.permission_classes = [IsStudentUser, IsOwnerProfile]
        else:
            # Permite realizar otras acciones solo a estudiantes
            self.permission_classes = [IsStudentUser]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        user = self.request.user

        if user.role == EduWorkUser.Role.STUDENT:
            return StudentProfile.objects.filter(user=user)

        if user.role == EduWorkUser.Role.COMPANY:
            if hasattr(user, 'company_profile'):
                return StudentProfile.objects.all()
            return StudentProfile.objects.none()

        if user.role == EduWorkUser.Role.ADMIN:
            return StudentProfile.objects.all()

        return StudentProfile.objects.none()
