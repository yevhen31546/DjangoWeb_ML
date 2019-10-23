# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 05:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0025_auto_20170926_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_subsciption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('subcription_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('unsubcription_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('unsubcription_reason', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
