# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0021_profile_referralcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='referralcode',
        ),
    ]
