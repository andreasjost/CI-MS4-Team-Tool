from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.planning, name='planning'),
    path('summary/<int:user_id>/', views.summary, name='summary'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('copy_event/', views.copy_event, name='copy_event'),
]
