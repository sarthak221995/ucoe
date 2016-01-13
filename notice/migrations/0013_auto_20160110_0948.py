# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0012_auto_20160108_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slide_image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slide_image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slide_image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='vision_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='vision_text',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_highlights',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
