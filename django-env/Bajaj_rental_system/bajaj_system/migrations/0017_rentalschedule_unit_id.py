# Generated by Django 5.0.3 on 2024-05-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0016_remove_rentalschedule_unit_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalschedule',
            name='unit_id',
            field=models.IntegerField(null=True),
        ),
    ]