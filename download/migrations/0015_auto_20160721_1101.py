# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0014_auto_20160204_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='previous_year',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'FIRSTSEMESTER', b'FIRST_SEMESTER'), (b'SECONDSEMESTER', b'SECOND_SEMESTER'), (b'THIRDSEMESTER', b'THIRD_SEMESTER'), (b'FOURTHSEMESTER', b'FOURTH_SEMESTER'), (b'FIFTHSEMESTER', b'FIFTH_SEMESTER'), (b'SIXTHSEMESTER', b'SIXTH_SEMESTER'), (b'SEVENTHSEMESTER', b'SEVENTH_SEMESTER'), (b'EIGHTSEMESTER', b'EIGHT_SEMESTER'), (b'MTECH', b'MTECH')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_table_year',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'FIRSTSEMESTER', b'FIRST_SEMESTER'), (b'SECONDSEMESTER', b'SECOND_SEMESTER'), (b'THIRDSEMESTER', b'THIRD_SEMESTER'), (b'FOURTHSEMESTER', b'FOURTH_SEMESTER'), (b'FIFTHSEMESTER', b'FIFTH_SEMESTER'), (b'SIXTHSEMESTER', b'SIXTH_SEMESTER'), (b'SEVENTHSEMESTER', b'SEVENTH_SEMESTER'), (b'EIGHTSEMESTER', b'EIGHT_SEMESTER'), (b'MTECH', b'MTECH')]),
        ),
    ]
