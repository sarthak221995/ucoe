# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0017_auto_20160204_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link_announcement',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link_notice',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
    ]
