from django.contrib import admin

from .models import AgentRole, Team


class AdminRole(admin.ModelAdmin):
        list_display = (
        'role_name',
        'role_color',
    )


class AdminTeam(admin.ModelAdmin):
    list_display = (
        'team_name',
        'planning_deadline',
        'coaching_rep',
        'min_lunchbreak',
        'min_dinnerbreak',
        'min_paidbreak',
    )

    ordering = ('team_name',)


admin.site.register(AgentRole, AdminRole)
admin.site.register(Team, AdminTeam)
