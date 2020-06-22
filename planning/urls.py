from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.planning, name='planning'),
    path('summary/<int:user_id>/', views.summary, name='summary'),
]
