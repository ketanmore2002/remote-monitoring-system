# Generated by Django 4.1.5 on 2023-08-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0014_remove_water_tank_run_time_today_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='water_tank_records',
            name='time',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='water_tank_records_temp',
            name='time',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
