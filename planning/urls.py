from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.planning, name='planning'),
    path('summary/<int:user_id>/', views.summary, name='summary'),
    path('month_change/<int:new_month>/', views.month_change, name='month_change'),
    path('month_current/', views.month_current, name='month_current'),
]
