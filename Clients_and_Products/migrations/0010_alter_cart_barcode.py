# Generated by Django 5.0 on 2024-02-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0009_cart_barcode_alter_order_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='barcode',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
