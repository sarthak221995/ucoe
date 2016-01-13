# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20160105_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='infra_image',
            field=models.ImageField(null=True, upload_to=b'images/about_images', blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='about',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_history',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='hostel',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='infra',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='labs',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
