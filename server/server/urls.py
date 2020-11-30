"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/auth/', include('authorization.urls')),
    url(r'^api/users/', include('user.urls')),
    url(r'^api/roles/', include('user.url_group')),
    url(r'^api/departments/', include('user.url_department')),
    url(r'^api/tickets/', include('ticket.urls')),
]