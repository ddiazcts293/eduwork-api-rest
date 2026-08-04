from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    CompanyRegisterView,
    StudentRegisterView,
    LogoutView,
    ChangePasswordView,
    ChangeEmailView,
    GetMeView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/company/', CompanyRegisterView.as_view(), name='register_company'),
    path('register/student/', StudentRegisterView.as_view(), name='register_student'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
    path('email/change/', ChangeEmailView.as_view(), name='change_email'),
    path('me/', GetMeView.as_view(), name='change_email'),
]
