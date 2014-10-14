# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from random import randint
import re


class Event(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    desc = models.TextField(blank=True, null=True)

    capacity = models.IntegerField()

    available_from = models.DateTimeField(blank=True, null=True)
    available_to = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def attendees(self, status):
        attendees = self.attendee_set.filter(status=status)
        if status == Attendee.SUBMITTED:
            attendees = attendees.order_by('id')
        elif status == Attendee.APPROVED:
            attendees = attendees.order_by('approved')
        return attendees

    @property
    def available(self):
        now = timezone.now()
        return self.available_from <= now <= self.available_to

    def __unicode__(self):
        return self.title


class Attendee(models.Model):
    SUBMITTED = 'SM'
    APPROVED = 'AP'
    CANCELED = 'CN'
    REJECTED = 'RJ'

    STATUS_CHOICES = (
        (SUBMITTED, u'등록'),
        (APPROVED, u'승인'),
        (CANCELED, u'취소'),
        (REJECTED, u'거절'),
    )

    event = models.ForeignKey(Event)

    email = models.EmailField()
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=SUBMITTED)
    checkkey = models.CharField(max_length=16, db_index=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    approved = models.DateTimeField(blank=True, null=True)

    @property
    def secret_email(self):
        m = re.match('([^@]+)@(.+)', self.email)
        if m:
            n = m.groups()
            return u'{}***@{}***'.format(
                n[0][:3],
                n[1][:3]
            )

        return u'{}**'.format(self.email[:3])

    def save(self, *args, **kwargs):
        while True:
            self.checkkey = u'{}{}'.format(self.name[:4], randint(1000, 9999))
            if not Attendee.objects.filter(checkkey=self.checkkey).exists():
                break
        super(Attendee, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.email)
