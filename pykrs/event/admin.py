from django.contrib import admin
from .models import Event, Attendee


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'capacity', 'available_from',
                    'available_to',)
    ordering = ('id',)
admin.site.register(Event, EventAdmin)


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'email', 'name', 'status', 'checkkey',
                    'created', 'approved')
    readonly_fields = ('checkkey',)
    ordering = ('id',)
admin.site.register(Attendee, AttendeeAdmin)
