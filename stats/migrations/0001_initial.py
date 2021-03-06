# Generated by Django 4.0.3 on 2022-04-20 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0)),
                ('done_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dispatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('staff_from', models.CharField(max_length=200)),
            ],
        ),
    ]
