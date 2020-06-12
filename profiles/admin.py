from django.contrib import admin

from .models import UserProfile

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
    )

    ordering = ('last_name',)


admin.site.register(UserProfile, ProfileAdmin)
