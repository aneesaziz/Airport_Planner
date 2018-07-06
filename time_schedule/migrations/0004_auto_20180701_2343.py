# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_schedule', '0003_auto_20180701_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hours_on_break',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='on_channel_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_of_relieve',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
