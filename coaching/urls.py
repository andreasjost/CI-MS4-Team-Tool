from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaching, name='coaching'),
    path('edit_session/<int:session_id>/', views.edit_session, name='edit_session'),
    path('add_session/', views.add_session, name='add_session'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
]
