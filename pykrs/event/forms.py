from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Attendee


class AttendeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttendeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Submit')))

    class Meta:
        model = Attendee
        fields = ('email', 'name', )
        labels = {
            'email': _('Email address'),
            'name': _('Name'),
        }
