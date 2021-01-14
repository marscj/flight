from django.http import HttpResponseRedirect
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly

from . import serializers
from . import models

class CheckVersion(APIView):

    def post(self, request, format=None):
        serializer = serializers.CheckVersionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        app = models.App.objects.filter(type=serializer.data['version']).last()
        
        if app is not None:
            if serializer.data['version'] == app.version:
                return Response({'result': True})
            else:
                return HttpResponseRedirect(redirect_to='https://google.com')
                # return Response({'result': False, 'url': app.file})
        
        return Response({'result': False, 'url': app.file})

class AppView(ModelViewSet):
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.App.objects.all().order_by('-id')