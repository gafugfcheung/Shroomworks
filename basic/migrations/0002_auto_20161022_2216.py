# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='pic',
            name='lng',
            field=models.FloatField(default=0.0),
        ),
    ]
