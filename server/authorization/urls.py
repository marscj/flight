from django.conf.urls import url

from .views import LoginView, LogoutView, UserInfoView, RegisterView, PasswordChangeView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^info/$', UserInfoView.as_view(), name='rest_user_details'),
    url(r'^registration/$', RegisterView.as_view(), name='rest_register'),
    url(r'^password/change/$', PasswordChangeView.as_view(),name='rest_password_change'),
]