from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('user_management/', views.user_management, name='user_management'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_user/', views.add_user, name='add_user'),
]
