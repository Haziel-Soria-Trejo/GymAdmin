# Generated by Django 4.0.3 on 2022-05-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_alter_activity_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('date',)},
        ),
    ]
