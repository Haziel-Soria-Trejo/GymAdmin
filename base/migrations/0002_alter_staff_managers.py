# Generated by Django 4.0.3 on 2022-04-15 23:18

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='staff',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
