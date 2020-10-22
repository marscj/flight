from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from .import views

router = DefaultRouter()
router.register(r'users', views.UserView, basename='users')

urlpatterns = [
    url(r'^user/login/$', views.CustomLoginView.as_view(), name='rest_login'),
    url(r'^user/logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/info/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^user/registration/$', views.CustomRegisterView.as_view(), name='rest_register'),
    url(r'^user/password/change/$', PasswordChangeView.as_view(),name='rest_password_change'),
]

urlpatterns = urlpatterns + router.urls