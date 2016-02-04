# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0013_post_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='people',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'STUDENTS', b'STUDENTS'), (b'FACULTY', b'FACULTY')]),
        ),
    ]
