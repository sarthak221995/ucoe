# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 1, 8, 8, 46, 35, 542000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
