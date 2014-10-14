from django.db import models
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
        return self.attendee_set.filter(status=status)

    def __unicode__(self):
        return self.title


class Attendee(models.Model):
    SUBMITTED = 'SM'
    APPROVED = 'AP'
    CANCELED = 'CN'
    REJECTED = 'RJ'

    STATUS_CHOICES = (
        (SUBMITTED, 'Submitted'),
        (APPROVED, 'Approved'),
        (CANCELED, 'Canceled'),
        (REJECTED, 'Rejected'),
    )

    event = models.ForeignKey(Event)

    email = models.EmailField()
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=SUBMITTED)
    checkkey = models.CharField(max_length=16)

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

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.email)
