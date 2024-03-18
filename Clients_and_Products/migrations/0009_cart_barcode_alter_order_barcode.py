# Generated by Django 5.0 on 2024-02-09 10:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0008_alter_order_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='barcode',
            field=models.CharField(default=uuid.uuid4, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='barcode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]