from django.http import HttpResponseRedirect
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions, IsAuthenticatedOrReadOnly

from . import serializers
from . import models

class CheckVersion(APIView):  
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        # serializer = serializers.CheckVersionSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        # app = models.App.objects.filter(type=serializer.data['type']).last()
        
        # if app is not None:
        #     if serializer.data['version'] == app.version:
        #         return Response({'result': True})
        #     else:
        #         if app.enable_redirect:
        #             return Response({'result': True, 'url': app.redirect})
        #         else:
        #             if app.file is not None:
        #                 return Response({'result': True, 'url': request.build_absolute_uri(app.file.url)}) 
        #             else:
        #                 return Response({'result': True})
        
        return Response({'result': True})

class AppView(ModelViewSet):
    serializer_class = serializers.AppSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = models.App.objects.all().order_by('-id')