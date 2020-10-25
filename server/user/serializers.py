from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_auth.serializers import LoginSerializer
from drf_recaptcha.fields import ReCaptchaV2Field, ReCaptchaV3Field

UserModel = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    
    backend = serializers.BooleanField(default=False)
    remember = serializers.BooleanField(default=True)
    # recaptcha = ReCaptchaV2Field(required=False)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs['user']

        if attrs['backend'] and not user.is_staff:
            raise PermissionDenied('You don\'t have permission to access.')

        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        exclude = ('password',)
        read_only_fields = ('email',)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        exclude = ('password',)
        read_only_fields = ('email',)