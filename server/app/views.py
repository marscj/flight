from django.http import HttpResponseRedirect
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly
import django_filters

from . import serializers
from . import models
    
class AppView(ModelViewSet):
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.App.objects.all().order_by('-id')

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def check_version(self, request, pk=None):
        type = self.request.query_params.get('type', None)

        if type is not None:
            data = models.App.objects.filter(type=type).last()

            if data is not None:
                serializer = serializers.AppSerializer(instance=data, context={'request': request})
                return Response(serializer.data)
        
        return Response({'code': 0})
