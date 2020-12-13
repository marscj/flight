from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
import django.contrib.auth.password_validation as validators
from django.core import exceptions

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.validators import UniqueValidator
from rest_auth.serializers import LoginSerializer as AuthLoginSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer

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

    name = serializers.CharField(required=False, max_length=150, validators=[UniqueValidator(queryset=Group.objects.all())])
    
    permission = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Group
        fields = '__all__'

    def update(self, instance, validated_data):
        permission = validated_data.pop('permission', None)
        
        if permission is not None:
            if instance.permissions.filter(id=permission).exists():
                instance.permissions.remove(permission)
            else:
                instance.permissions.add(permission)

        return super().update(instance, validated_data)

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

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        password = data.get('password', None)
        
        if password:
            validators.validate_password(password=password)
        
        return super().validate(data)

class UserListSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()

    roles = ListGroupSerializer(read_only=True, many=True, source='groups')

    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'name', 'email', 'roles', 'is_staff', 'is_active', 'department', 'passport_no', 'avatar'
        )
        read_only_fields = ('id', 'email', 'is_staff', 'is_active')

    def get_name(self, obj):
        return obj.full_name or obj.email

class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    roles = GroupSerializer(read_only=True, many=True, source='groups')

    department_id = serializers.IntegerField(required=False, allow_null=True)

    department = serializers.StringRelatedField(read_only=True)

    groups_id = serializers.PrimaryKeyRelatedField(required=False, many=True, allow_null=True, queryset=Group.objects.all(), source='groups')

    avatar = VersatileImageFieldSerializer(required=False, allow_null=True, sizes='image_size', read_only=False)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'first_name', 'last_name', 'roles', 'is_active', 'is_staff', 'is_superuser',
            'possport_type', 'passport_code', 'passport_no', 'passport_sex', 'passport_nationality', 'passport_date_birth',
            'passport_place_birth', 'passport_date_issue', 'passport_date_expiry', 'passport_issuing_authority',
            'name', 'department_id', 'groups_id', 'department', 'avatar'
        )
        read_only_fields = ('username', 'password', 'email', 'last_login', 'is_superuser', 'date_joined', 'department', 'avatar')

    def get_name(self, obj):
        return obj.full_name

    def update(self, instance, validated_data):

        if not self.context['request'].user.has_perm('user.assign_role'):
            validated_data.pop('groups', None)
        
        return super().update(instance, validated_data)