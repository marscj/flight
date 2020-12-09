from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BookingView, BookingHistoryView, ItineraryView, ItineraryHistoryView

router = DefaultRouter()
router.register('bookings', BookingView, basename='bookings')
router.register('booking/histories', BookingHistoryView, basename='booking_history')
router.register('itineraries', ItineraryView, basename='itineraries')
router.register('itinerary/histories', ItineraryHistoryView, basename='itinerary_history')
urlpatterns = router.urls