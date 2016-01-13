# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploads/placement-rec', blank=True)),
                ('placement_year', models.CharField(max_length=200, null=True, blank=True)),
                ('placement_recfile', models.FileField(null=True, upload_to=b'uploads/placement-rec', blank=True)),
                ('companies_logo', models.ImageField(null=True, upload_to=b'uploads/placement-rec', blank=True)),
            ],
        ),
    ]
