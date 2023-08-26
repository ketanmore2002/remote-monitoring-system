# Generated by Django 4.1.5 on 2023-08-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0012_water_tank_records_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water_tank',
            name='signal_strength',
        ),
        migrations.AddField(
            model_name='water_tank_records',
            name='signal_strength',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='water_tank_records_temp',
            name='signal_strength',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]