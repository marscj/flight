from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BookingView, BookingHistoryView

router = DefaultRouter()
router.register(r'', BookingView, basename='bookings')
urlpatterns = router.urls