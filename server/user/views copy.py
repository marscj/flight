from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.conf import settings


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
import django_filters 
from rest_auth.registration.app_settings import RegisterSerializer

from . import serializers, models
from middleware import viewset, permissions
from authorization.views import RegisterView

UserModel = get_user_model()

class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id', )
    role = django_filters.NumberFilter('groups__id')
    department = django_filters.NumberFilter('department_id')
    is_staff = django_filters.BooleanFilter('is_staff')
    is_active = django_filters.BooleanFilter('is_active')

class UserView(viewset.ExtraModelViewSet, RegisterView):
    serializer_class = serializers.UserDetailsSerializer
    list_serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, permissions.ModelPermissions]
    queryset = UserModel.objects.all().order_by('id')

    filter_class = UserFilter
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer

        return super().get_serializer_class()

    def get_extra_data(self, request):
        return {
            'role': serializers.ListGroupSerializer(Group.objects.all(), many=True, context={'request': request}).data,
            'department': serializers.DepartmentSerializer(models.Department.objects.all(), many=True, context={'request': request}).data
        }

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, permissions.ResetPasswordPermission])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        serializer = serializers.PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
 
class GroupFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')

class GroupView(viewset.ExtraModelViewSet):
    serializer_class = serializers.GroupSerializer
    list_serializer_class = serializers.ListGroupSerializer
    permission_classes = [IsAuthenticated, permissions.ModelPermissions]
    queryset = Group.objects.all().order_by('id')
 
    filter_class = GroupFilter
    search_fields = ['name']

    def get_extra_data(self, request):
        queryset = Permission.objects.filter(content_type__model__in=['user', 'department', 'group', 'booking', 'itinerary', 'ticket', 'comment', 'historicalbooking'])
        return {
            'permission': serializers.PermissionSerializer(queryset, many=True, context={'request': request}).data,
        }


class DepartmentFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter('id')

class DepartmentView(viewset.ExtraModelViewSet):
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticated, permissions.ModelPermissions]
    queryset = models.Department.objects.all().order_by('id')
 
    filter_class = DepartmentFilter
    search_fields = ['name']