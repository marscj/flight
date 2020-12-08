from rest_framework import status
from rest_framework.response import Response

class ExtraListModelMixin:
    
    list_serializer_class = None

    def get_serializer_class(self):        
        if self.action == 'list' and self.list_serializer_class is not None:
            return self.list_serializer_class

        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            
            return Response({
                'data': self.paginator.get_paginated_data(serializer.data),
                'extra': self.get_extra_data()
            })

        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_data()
        })

class ExtraRetrieveModelMixin:

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_data()
        })

class ExtraUpdateModelMixin:

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({
            'data': serializer.data,
            'extra': self.get_extra_data()
        })

class CreateModelMixin:
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_data()
        }, status=status.HTTP_201_CREATED, headers=headers)