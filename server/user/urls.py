from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import UserView

router = DefaultRouter()
router.register(r'', UserView, basename='users')
urlpatterns = router.urls