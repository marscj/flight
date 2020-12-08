from rest_framework.viewsets import ModelViewSet
from . import mixins

class ExtraModelViewSet(mixins.CreateModelMixin,
                   mixins.ExtraRetrieveModelMixin,
                   mixins.ExtraUpdateModelMixin,
                   mixins.ExtraListModelMixin,
                   ModelViewSet):
    
    extra_data = None
    history_data = None

    def get_extra_data(self):
        return self.extra_data

    def get_history_data(self):
        return self.history_data



