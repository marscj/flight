from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import ItineraryView

router = DefaultRouter()
router.register(r'', ItineraryView, basename='Itineraries')
urlpatterns = router.urls