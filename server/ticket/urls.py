from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BookingView, BookingHistoryView, ItineraryView

router = DefaultRouter()
router.register('bookings', BookingView, basename='bookings')
router.register('booking/histories', BookingHistoryView, basename='bookings')
router.register('itineraries', ItineraryView, basename='bookings')
urlpatterns = router.urls