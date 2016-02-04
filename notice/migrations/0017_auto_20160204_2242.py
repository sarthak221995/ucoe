# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0016_auto_20160112_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_announcement',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link_notice',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
