from django.urls import path
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CompanyRegisterView, StudentRegisterView

urlpatterns = [
    # Los endpoints por defecto para hacer login y refrescar token
    #path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/company/', CompanyRegisterView.as_view(), name='register_company'),
    path('register/student/', StudentRegisterView.as_view(), name='register_student'),
]
