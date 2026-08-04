from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.company_serializers import CompanyRegistrationSerializer
from .serializers.student_serializers import StudentRegistrationSerializer
from .serializers.change_password_serializer import ChangePasswordSerializer

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
        refresh = RefreshToken.for_user(user)

        # Responde con un mensaje de éxito
        return Response({
            "message": "Company registered successfully",
            "user_id": user.id,
            "email": user.email,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
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
        refresh = RefreshToken.for_user(user)

        # Responde con un mensaje de éxito
        return Response({
            "message": "Student registered successfully",
            "user_id": user.id,
            "email": user.email,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {'message': 'Logout successfully'},
                status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['put']

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Verifica la contraseña actual
        if not user.check_password(serializer.validated_data.get("old_password")):
            return Response({"message": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)

        # Establece la nueva contraseña
        user.set_password(serializer.validated_data.get("new_password"))
        user.save()

        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
