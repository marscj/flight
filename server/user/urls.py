from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import UserView, GroupView, DepartmentView

router = DefaultRouter()
router.register('users', UserView, basename='users')
router.register('roles', GroupView, basename='roles')
router.register('departments', DepartmentView, basename='departments')
urlpatterns = router.urls