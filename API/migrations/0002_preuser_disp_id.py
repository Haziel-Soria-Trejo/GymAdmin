# Generated by Django 4.0.3 on 2022-04-23 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_dispatches_subject'),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preuser',
            name='disp_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stats.dispatches'),
        ),
    ]