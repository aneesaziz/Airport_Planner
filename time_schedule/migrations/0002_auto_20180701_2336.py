# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hours_on_break',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='on_channel_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_of_relieve',
            field=models.DateTimeField(null=True),
        ),
    ]
