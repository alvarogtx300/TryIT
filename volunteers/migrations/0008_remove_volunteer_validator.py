# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0007_auto_20180307_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='validator',
        ),
    ]