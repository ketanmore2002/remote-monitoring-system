# Generated by Django 4.1.5 on 2023-08-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0009_water_tank_records_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='water_tank_records',
            name='present_lpm',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]