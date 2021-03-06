from django.urls import path
from . import views
from settings.webhooks import webhook

urlpatterns = [
    path('global/', views.settings_global, name='settings_global'),
    path('shifts/', views.shifts, name='shifts'),
    path('edit_shift/<int:shift_id>/', views.edit_shift, name='edit_shift'),
    path('add_shift/', views.add_shift, name='add_shift'),
    path('teams/', views.teams, name='teams'),
    path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
    path('add_team/', views.add_team, name='add_team'),
    path('change_plan/', views.change_plan, name='change_plan'),
    path('wh/', webhook, name='webhook'),
]

# disabled roles due to time pressure. Left to resume later:
"""
path('roles/', views.roles, name='roles'),
path('edit_role/<int:role_id>/', views.edit_role, name='edit_role'),
path('add_role/', views.add_role, name='add_role'),
"""
