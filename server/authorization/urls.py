from django.conf.urls import url

from .views import LoginView, LogoutView, UserInfoView, RegisterView, PasswordChangeView

urlpatterns = [
    url('auth/login/', LoginView.as_view(), name='rest_login'),
    url('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    url('auth/info/', UserInfoView.as_view(), name='rest_user_details'),
    url('auth/registration/', RegisterView.as_view(), name='rest_register'),
    url('auth/password/change/', PasswordChangeView.as_view(),name='rest_password_change'),
]