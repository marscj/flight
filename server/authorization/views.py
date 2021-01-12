from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework.response import Response
from rest_framework import throttling
from rest_auth.views import (
    LoginView as AuthLoginView, 
    LogoutView as AuthLogoutView, 
    UserDetailsView, 
    PasswordChangeView as AuthPasswordChangeView 
)
from rest_auth.registration.views import RegisterView as AuthRegisterView

from plugs import message

UserModel = get_user_model()

class LoginView(AuthLoginView):
    throttle_classes = [throttling.AnonRateThrottle]    

class RegisterView(AuthRegisterView):
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        message.create.delay(serializer.email, serializer.password1)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)
        
class LogoutView(AuthLogoutView):
    pass

class UserInfoView(UserDetailsView):
    pass

class PasswordChangeView(AuthPasswordChangeView):
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        message.update_password.delay(request.user, serializer.password1)
        return Response({"detail": _("New password has been saved.")})
