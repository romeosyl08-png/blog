from django.contrib import admin
from django.urls import include, path

from .views import register

app_name = 'users'


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]