# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_volunteer_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='android_phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='shirt_size',
            field=models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], default='M', max_length=250),
        ),
    ]