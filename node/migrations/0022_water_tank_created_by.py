# Generated by Django 4.1.5 on 2023-08-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0021_water_tank_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='water_tank',
            name='created_by',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]