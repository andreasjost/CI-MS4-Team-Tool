from django.contrib import admin

from .models import Event, EventCategory


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


class AdminEventCategory(admin.ModelAdmin):
        list_display = (
        'category',
        'color',
    )


admin.site.register(Event, AdminEvent)
admin.site.register(EventCategory, AdminEventCategory)