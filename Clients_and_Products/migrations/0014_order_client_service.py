# Generated by Django 5.0 on 2024-02-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0013_alter_cart_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_service',
            field=models.CharField(default='000 208 0660', max_length=20),
        ),
    ]
