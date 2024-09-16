# Generated by Django 2.1.7 on 2019-03-21 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_attendant_registered_as_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendant',
            name='ects',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(3.0)]),
        ),
    ]
