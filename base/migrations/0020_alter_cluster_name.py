# Generated by Django 4.0.3 on 2022-05-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_client_paid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
