# Generated by Django 4.0.3 on 2022-04-20 22:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
