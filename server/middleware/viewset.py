from rest_framework.viewsets import ModelViewSet
from . import mixins

class ExtraModelViewSet(mixins.CreateModelMixin,
                   mixins.ExtraRetrieveModelMixin,
                   mixins.ExtraUpdateModelMixin,
                   mixins.ExtraListModelMixin,
                   ModelViewSet):
    
    extra_data = None
    
    def get_extra_data(self):
        return extra_data