# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='checkkey',
            field=models.CharField(max_length=16, db_index=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='status',
            field=models.CharField(default=b'SM', max_length=2, choices=[(b'SM', '\ub4f1\ub85d'), (b'AP', '\uc2b9\uc778'), (b'CN', '\ucde8\uc18c'), (b'RJ', '\uac70\uc808')]),
        ),
    ]
