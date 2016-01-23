# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_college', models.ImageField(blank=True, null=True, upload_to='campus')),
                ('gallery_labs', models.ImageField(blank=True, null=True, upload_to='campus')),
                ('gallery_hostel', models.ImageField(blank=True, null=True, upload_to='campus')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
