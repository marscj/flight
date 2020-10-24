from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
import django_filters

from . import serializers

UserModel = get_user_model()

class CustomLoginView(LoginView):
    throttle_classes = [throttling.AnonRateThrottle]

    # def post(self, request, pk=None):
    #     serializer = serializers.LoginSerializer(data=request.data, context={"request": request})
    #     serializer.is_valid(raise_exception=True)
    #     print(serializer)
    #     return Response('ok')

class CustomRegisterView(RegisterView):
    queryset = UserModel.objects.all()

class UserFilter(django_filters.FilterSet):
    role = django_filters.NumberFilter('role')

class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = UserModel.objects.filter(is_delete=False)
 
    filter_class = UserFilter
    search_fields = ['email', 'first_name', 'last_name', 'passport_no']
 
