# Generated by Django 5.0.3 on 2024-05-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerou', '0003_item_remove_order_od_product_remove_order_od_useracc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]