from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Attendee


class EventAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'capacity', 'available_from',
                    'available_to',)
    ordering = ('id',)
admin.site.register(Event, EventAdmin)


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'email', 'name', 'status', 'checkkey',
                    'created', 'approved', 'note',)
    readonly_fields = ('checkkey',)
    ordering = ('id',)
admin.site.register(Attendee, AttendeeAdmin)
