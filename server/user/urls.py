from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from rest_auth.views import (LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from .views import UserView, LoginView, RegisterView

router = DefaultRouter()
router.register(r'users', UserView, basename='users')

urlpatterns = [
    url(r'^user/login/$', LoginView.as_view(), name='rest_login'),
    url(r'^user/logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/info/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^user/registration/$', RegisterView.as_view(), name='rest_register'),
    url(r'^user/password/change/$', PasswordChangeView.as_view(),name='rest_password_change'),
]

urlpatterns = urlpatterns + router.urls