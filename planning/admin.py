from django.contrib import admin

from .models import Event


class AdminEvent(admin.ModelAdmin):
    list_display = (
        'user_id',
        'category',
        'date',
        'start_time',
        'end_time',
        'agent_role',
        'status',
    )


admin.site.register(Event, AdminEvent)
