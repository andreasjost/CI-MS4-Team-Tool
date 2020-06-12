from django.urls import path
from . import views

urlpatterns = [
    path('global/', views.settings_global, name='settings_global'),
    path('team/', views.settings_team, name='settings_team'),
]