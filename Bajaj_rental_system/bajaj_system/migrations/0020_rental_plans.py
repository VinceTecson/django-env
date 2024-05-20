# Generated by Django 5.0.3 on 2024-05-07 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0019_rentalrecord_present_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental_Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('plan_description', models.CharField(max_length=200)),
                ('plan_hours', models.IntegerField(null=True)),
                ('plan_cost', models.IntegerField(null=True)),
                ('plan_units', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bajaj_system.units')),
            ],
        ),
    ]