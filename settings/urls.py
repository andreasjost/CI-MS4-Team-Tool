from django.urls import path
from . import views

urlpatterns = [
    path('global/', views.settings_global, name='settings_global'),
    path('shifts/', views.shifts, name='shifts'),
    path('roles/', views.shifts, name='roles'),
    path('teams/', views.teams, name='teams'),
    path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
    path('add_team/', views.add_team, name='add_team'),
]