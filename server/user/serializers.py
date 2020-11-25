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

    content_type = ContentTypeSerializer(many=False)

    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    
    permissions = PermissionSerializer(read_only=True, many=True)

    name = serializers.CharField(required=False, max_length=150)
    
    class Meta:
        model = Group
        fields = '__all__'

class LoginSerializer(AuthLoginSerializer):
    
    backend = serializers.BooleanField(default=False)

    def validate(self, attrs):
        attrs = super().validate(attrs) 
        user = attrs['user']

        if attrs['backend'] and not user.is_staff:
            raise PermissionDenied({'non_field_errors': ['You don\'t have permission to access.']})

        return attrs

class UserDetailsSerializer(serializers.ModelSerializer):

    roles = GroupSerializer(many=True, source='groups')

    name = serializers.SerializerMethodField()
    
    class Meta:
        model = UserModel
        fields = (
            'id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'name', 'email', 'is_staff', 'is_active', 'date_joined',
            'possport_type', 'passport_code', 'passport_no', 'passport_sex', 'passport_nationality', 'passport_date_birth',
            'passport_place_birth', 'passport_date_issue', 'passport_date_expiry', 'passport_issuing_authority',
            'avatar', 'is_delete', 'department', 'roles'
        )
        read_only_fields = ('username', 'password', 'email', 'name', 'department', 'roles', 'last_login', 'is_superuser', 'date_joined')

    def get_name(self, obj):
        if obj.full_name:
            return obj.full_name
        return obj.username

class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()

    roles = serializers.StringRelatedField(read_only=True, many=True, source='groups')

    department = serializers.SerializerMethodField()

    department_id = serializers.PrimaryKeyRelatedField(required=False, allow_null=True, queryset=Department.objects.all())

    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('username', 'password', 'email', 'last_login', 'is_superuser', 'date_joined')

    def get_name(self, obj):
        return obj.full_name

    def get_department(self, obj):
        try:
            department = Department.objects.all()
            serializers = DepartmentSerializer(instance=department, many=True, context=self.context)
            return serializers.data
        except Department.DoesNotExist:
            return []

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data.pop('groups', None)
        print('------------')
        print(validated_data)
        return super().update(instance, validated_data)
