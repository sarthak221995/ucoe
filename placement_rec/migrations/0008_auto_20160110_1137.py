# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('placement_rec', '0007_auto_20160110_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='companies_logo',
            field=models.ImageField(upload_to=b'uploads/placement-rec'),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.CharField(default=datetime.datetime(2016, 1, 10, 6, 7, 58, 622000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
