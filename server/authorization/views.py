from django.contrib.auth import get_user_model

from rest_framework import throttling
from rest_auth.views import (
    LoginView as AuthLoginView, 
    LogoutView as AuthLogoutView, 
    UserDetailsView, 
    PasswordChangeView as AuthPasswordChangeView 
)
from rest_auth.registration.views import RegisterView as AuthRegisterView

UserModel = get_user_model()

class LoginView(AuthLoginView):
    throttle_classes = [throttling.AnonRateThrottle]    

class RegisterView(AuthRegisterView):
    pass

class LogoutView(AuthLogoutView):
    pass

class UserInfoView(UserDetailsView):
    pass

class PasswordChangeView(AuthPasswordChangeView):
    pass