# Generated by Django 4.1.5 on 2023-08-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0013_remove_water_tank_signal_strength_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water_tank',
            name='run_time_today',
        ),
        migrations.AddField(
            model_name='water_tank_records',
            name='run_time_today',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='water_tank_records_temp',
            name='run_time_today',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
