from django.contrib import admin

from .models import CompanyProfile, AgentRole, Team


class AdminCompany(admin.ModelAdmin):
    list_display = (
        'company_name',
        'street_address1',
        'street_address2',
        'country',
        'postcode',
        'town_or_city',
        'plan',
        'signup_date',
        'renewal_date',
        'payment',
        'setting_weekstart',
    )

    ordering = ('company_name',)


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


admin.site.register(CompanyProfile, AdminCompany)
admin.site.register(AgentRole, AdminRole)
admin.site.register(Team, AdminTeam)
