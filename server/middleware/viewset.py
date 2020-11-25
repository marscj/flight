from rest_framework.viewsets import ModelViewSet

class ExtraModelViewSet(ModelViewSet):

    list_serializer_class = None
    
    def get_extra_data(self, request):
        return []

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