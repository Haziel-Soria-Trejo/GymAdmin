# Generated by Django 4.0.3 on 2022-04-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_client_register_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=2),
        ),
    ]