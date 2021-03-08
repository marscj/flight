from django.http import HttpResponseRedirect
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly

from . import serializers
from . import models

class AppView(ModelViewSet):
    serializer_class = serializers.AppSerializer
    permission_classes = [AllowAny]
    queryset = models.App.objects.all().order_by('-id')