from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_auth.serializers import LoginSerializer

UserModel = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs['user']

        if not user.is_staff:
            raise serializers.ValidationError('You don\'t have permission to access.')

        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        exclude = ('password',)
        read_only_fields = ('email', )