# Generated by Django 5.0.3 on 2024-04-27 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0005_remove_customer_ct_useracc_useracc_user_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useracc',
            name='user_customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='ct_userAcc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bajaj_system.useracc'),
        ),
    ]
