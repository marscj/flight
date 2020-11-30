from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'bookings', views.BookingView, basename='bookings')
urlpatterns = router.urls