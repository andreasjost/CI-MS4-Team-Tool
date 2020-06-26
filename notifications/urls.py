from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
]
