# Generated by Django 2.1.7 on 2020-02-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0010_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='edition',
            field=models.ManyToManyField(to='editions.Edition'),
        ),
    ]
