# Generated by Django 4.1.5 on 2023-08-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0020_water_tank_site_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='water_tank',
            name='state',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]