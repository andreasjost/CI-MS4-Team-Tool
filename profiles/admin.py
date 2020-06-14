from django.contrib import admin

from .models import UserProfile, CompanyProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday_ddmm',
        'start_date',
        'end_date',
        'level',
        'role',
        'team',
        'contract_type',
        'contract_percentage',
        'agent_goal',
        'company_id'
    )

    ordering = ('last_name',)


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


admin.site.register(CompanyProfile, AdminCompany)
admin.site.register(UserProfile, ProfileAdmin)
