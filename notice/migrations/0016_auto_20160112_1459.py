# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0015_auto_20160112_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
