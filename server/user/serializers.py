from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_auth.serializers import LoginSerializer as AuthLoginSerializer
from .models import Department

UserModel = get_user_model()

class DepartmentSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length=32)

    class Meta:
        model = Department
        fields = '__all__'

class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)

    codename = serializers.CharField(max_length=100)

    content_type = ContentTypeSerializer()

    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    
    permissions = PermissionSerializer(read_only=True, many=True)

    name = serializers.CharField(max_length=150)
    
    class Meta:
        model = Group
        fields = '__all__'

class ListGroupSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    
    class Meta:
        model = Group
        fields = ('id', 'name')

class LoginSerializer(AuthLoginSerializer):
    
    backend = serializers.BooleanField(default=False)

    def validate(self, attrs):
        attrs = super().validate(attrs) 
        user = attrs['user']

        if attrs['backend'] and not user.is_staff:
            raise PermissionDenied({'non_field_errors': ['You don\'t have permission to access.']})

        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    roles = GroupSerializer(read_only=True, many=True, source='groups')

    department = serializers.SerializerMethodField()

    department_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, queryset=Department.objects.all())

    class Meta:
        model = UserModel
        exclude = (
            'groups', 'user_permissions'
        )
        read_only_fields = ('username', 'password', 'email', 'last_login', 'is_superuser', 'date_joined')

    def get_name(self, obj):
        return obj.full_name

    def get_department(self, obj):
        department = Department.objects.all()
        serializers = DepartmentSerializer(instance=department, many=True, context=self.context)
        return serializers.data

class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()

    roles = ListGroupSerializer(read_only=True, many=True, source='groups')

    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'name', 'email', 'roles', 'is_staff', 'is_active', 'department'
        )
        read_only_fields = ('id', 'email', 'is_staff', 'is_active')

    def get_name(self, obj):
        return obj.full_name