from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BookingView, BookingHistoryView, ItineraryView, ItineraryHistoryView, TicketView, TicketHistoryView, MessageView, UpLoadView

router = DefaultRouter()
router.register('bookings', BookingView, basename='bookings')
router.register('booking/histories', BookingHistoryView, basename='booking_history')
router.register('itineraries', ItineraryView, basename='itineraries')
router.register('itinerary/histories', ItineraryHistoryView, basename='itinerary_history')
router.register('tickets', TicketView, basename='tickets')
router.register('ticket/histories', TicketHistoryView, basename='ticket_history')
router.register('messages', MessageView, basename='messages')
router.register('uploads', UpLoadView, basename='uploads')
urlpatterns = router.urls