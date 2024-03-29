# Generated by Django 4.1.5 on 2023-11-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0025_alter_water_tank_pump_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water_tank',
            name='rms',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records',
            name='rms',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='water_tank_records_temp',
            name='rms',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]
