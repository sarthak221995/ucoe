# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0006_auto_20160114_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='previous_year',
            field=models.CharField(blank=True, choices=[('FIRST YEAR', 'FIRST_YEAR'), ('SECOND YEAR', 'SECOND_YEAR'), ('THIRD YEAR', 'THIRD_YEAR'), ('FOURTH YEAR', 'FOURTH_YEAR')], max_length=20, null=True),
        ),
    ]
