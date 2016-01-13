# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement_rec', '0002_auto_20160109_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_head',
        ),
    ]
