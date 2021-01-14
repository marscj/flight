from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('apps', views.AppView, basename='apps')

urlpatterns = [
    url('version/', views.CheckVersion.as_view(), name='version'),
]

urlpatterns = urlpatterns + router.urls