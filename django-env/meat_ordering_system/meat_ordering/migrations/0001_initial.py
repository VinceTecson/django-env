# Generated by Django 5.0.4 on 2024-05-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
