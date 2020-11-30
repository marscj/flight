from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import DepartmentView

router = DefaultRouter()
router.register(r'', DepartmentView, basename='departments')
urlpatterns = router.urls