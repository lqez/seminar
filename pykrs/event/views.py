# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Event, Attendee
from .forms import AttendeeForm


def index(request):
    event = Event.objects.get(id=1)
    form = AttendeeForm(initial={'event': event})
    warning = None

    if request.method == 'POST':
        form = AttendeeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            if not event.available:
                warning = u'이벤트 신청 기간이 아닙니다.'
            elif Attendee.objects.filter(email=email).exists():
                warning = u'이미 등록된 이메일 입니다.'
            else:
                attendee = Attendee(email=email, name=name, event=event)
                attendee.save()

                return render(request, 'registered.html', {
                    'event': event,
                    'attendee': attendee,
                })

    return render(request, 'index.html', {
        'event': event,
        'form': form,
        'warning': warning,
        'attendees': {
            'submitted': event.attendees(Attendee.SUBMITTED),
            'approved': event.attendees(Attendee.APPROVED),
        },
    })
