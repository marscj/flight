from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_auth.serializers import LoginSerializer
from drf_recaptcha.fields import ReCaptchaV2Field, ReCaptchaV3Field

UserModel = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    
    backend = serializers.BooleanField(default=False)
    remember = serializers.BooleanField(default=True)

    if not settings.DEBUG:
        recaptcha = ReCaptchaV2Field(required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs) 
        user = attrs['user']

        if attrs['backend'] and not user.is_staff:
            raise PermissionDenied({'non_field_errors': ['You don\'t have permission to access.']})

        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = (
            'id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined',
            'possport_type', 'passport_code', 'passport_no', 'passport_sex', 'passport_nationality', 'passport_date_birth',
            'passport_place_birth', 'passport_date_issue', 'passport_date_expiry', 'passport_issuing_authority',
            'role', 'avatar', 'is_delete', 'department', 'groups', 'user_permissions'
        )
        read_only_fields = ('username','email', 'full_name', 'department', 'groups', 'user_permissions')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        exclude = ('password',)
        read_only_fields = ('email',)