# Generated by Django 4.0.3 on 2022-05-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_dispatches_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]