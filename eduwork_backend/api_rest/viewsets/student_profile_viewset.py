from rest_framework import viewsets
from ..models import StudentProfile
from ..serializers.student_profile_serializer import StudentProfileSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
