# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Attendee


class AttendeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttendeeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', u'참가 등록'))

    class Meta:
        model = Attendee
        fields = ('email', 'name', 'event')
        labels = {
            'email': u'이메일 주소',
            'name': u'이름',
        }
        widgets = {
            'event': forms.HiddenInput(),
        }
