# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 14:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_extended', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Date_of_visit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='No_of_offer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Organization',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='compensation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=datetime.datetime(2016, 1, 11, 14, 47, 17, 305516, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='placement_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
