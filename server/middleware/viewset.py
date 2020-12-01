from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class ExtraModelViewSet(ModelViewSet):

    list_serializer_class = None
    
    def get_extra_data(self, request):
        return {}

    def get_history_data(self, request):
        return {}

    def get_serializer_class(self):
        
        if self.action == 'list' and self.list_serializer_class is not None:
            return self.list_serializer_class

        return super().get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.paginator.get_extra_paginated_response(serializer.data, self.get_extra_data(request))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        return Response({
            'data': serializer.data,
            'extra': self.get_extra_data(request),
            'history': self.get_history_data(request)
        })

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
            'extra': self.get_extra_data(request)
        })