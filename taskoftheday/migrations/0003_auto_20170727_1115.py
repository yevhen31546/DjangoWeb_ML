# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-07-27 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taskoftheday', '0002_auto_20170726_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='step',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]