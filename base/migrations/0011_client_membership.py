# Generated by Django 4.0.3 on 2022-04-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_expenses_inventory_price_task_is_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='membership',
            field=models.CharField(choices=[('month', 'month'), ('week', 'week'), ('visit', 'visit')], default='month', max_length=50),
        ),
    ]
