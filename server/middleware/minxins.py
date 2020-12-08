from rest_framework import status
from rest_framework.response import Response

class ExtraListModelMixin:
    
    extra_list_data = None

    def get_extra_list_data(self):
        return self.extra_list_data

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_list_data()
        })

class ExtraRetrieveModelMixin:
    
    extra_retrieve_data = None

    def get_extra_retrieve_data(self):
        return self.extra_retrieve_data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_retrieve_data()
        })