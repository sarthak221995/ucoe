# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0012_auto_20160114_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='people',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'STUDENTS', b'STUDENTS'), (b'FACULTY', b'STUDENTS')]),
        ),
    ]
