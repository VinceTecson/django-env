# Generated by Django 5.0.3 on 2024-05-18 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0030_alter_contact_message_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units_conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdt_unit_condition', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='units',
            name='unit_cdt_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bajaj_system.units_conditions'),
        ),
    ]
