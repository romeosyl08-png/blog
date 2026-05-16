from django.contrib import admin
from django.urls import include, path

from .views import about, homepage, post_create, post_details, post_edit ,post_delete

app_name = 'home'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('posts/<int:pk>/', post_details, name='post_details'),
    path('posts/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('about/', about, name='about'),
    
]