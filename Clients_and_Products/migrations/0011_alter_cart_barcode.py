# Generated by Django 5.0 on 2024-02-09 10:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0010_alter_cart_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='barcode',
            field=models.CharField(default=uuid.uuid4, max_length=200),
        ),
    ]
