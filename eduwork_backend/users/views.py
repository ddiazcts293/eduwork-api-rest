from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.company_serializers import CompanyRegistrationSerializer
from .serializers.student_serializers import StudentRegistrationSerializer

# Create your views here.

User = get_user_model()

class CompanyRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Permite el registro sin haber iniciado sesión
    serializer_class = CompanyRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Crea el token JWT para este usuario nuevo
        #refresh = RefreshToken.for_user(user)

        # Responde con un mensaje de éxito
        return Response({
            "message": "Company registered successfully",
            "user_id": user.id,
            "email": user.email,
            "tokens": {
                #"refresh": str(refresh),
                #"access": str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)

class StudentRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Permite el registro sin haber iniciado sesión
    serializer_class = StudentRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Crea el token JWT para este usuario nuevo
        #refresh = RefreshToken.for_user(user)

        # Responde con un mensaje de éxito
        return Response({
            "message": "Student registered successfully",
            "user_id": user.id,
            "email": user.email,
            "tokens": {
                #"refresh": str(refresh),
                #"access": str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
