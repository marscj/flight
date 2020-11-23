from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import GroupView

router = DefaultRouter()
router.register(r'', GroupView, basename='roles')
urlpatterns = router.urls