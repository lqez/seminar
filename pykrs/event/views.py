from django.shortcuts import render
from .models import Event, Attendee
from .forms import AttendeeForm


def index(request):
    event = Event.objects.get(id=1)

    return render(request, 'index.html', {
        'event': event,
        'form': AttendeeForm(),
        'attendees': {
            'submitted': event.attendees(Attendee.SUBMITTED),
            'approved': event.attendees(Attendee.APPROVED),
        },
    })
