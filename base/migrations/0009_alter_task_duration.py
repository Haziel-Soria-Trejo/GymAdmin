# Generated by Django 4.0.3 on 2022-04-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_task_duration_alter_task_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.TimeField(),
        ),
    ]
