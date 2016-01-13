# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement_rec', '0005_auto_20160109_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='placement_recfile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='placement_year',
        ),
    ]
