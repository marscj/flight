from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.validators import UniqueValidator
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

class UserDetailsSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    roles = GroupSerializer(read_only=True, many=True, source='groups')

    department_id = serializers.IntegerField(required=False, allow_null=True)

    groups_id = serializers.PrimaryKeyRelatedField(required=False, many=True, allow_null=True, queryset=Group.objects.all(), source='groups')

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'first_name', 'last_name', 'roles', 'is_active', 'is_staff', 
            'possport_type', 'passport_code', 'passport_no', 'passport_sex', 'passport_nationality', 'passport_date_birth',
            'passport_place_birth', 'passport_date_issue', 'passport_date_expiry', 'passport_issuing_authority',
            'avatar', 'is_delete', 'name', 'department_id', 'groups_id'
        )
        read_only_fields = ('username', 'password', 'email', 'last_login', 'is_superuser', 'date_joined')

    def get_name(self, obj):
        return obj.full_name

    def update(self, instance, validated_data):
        groups_id = validated_data.pop('groups_id', None)
        print(groups_id)
        if groups_id is not None:
            for group in list(instance.groups.all()):
                instance.groups.remove(group)
                    
            for id in groups_id:
                instance.groups.add(id)

        return super().update(instance, validated_data)

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