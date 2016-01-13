# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('placement_rec', '0006_auto_20160110_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 5, 58, 14, 627000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='logo',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 5, 58, 18, 781000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
