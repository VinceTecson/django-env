# Generated by Django 5.0.3 on 2024-05-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0023_rename_ct_password_customer_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalschedule',
            name='rs_plan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
