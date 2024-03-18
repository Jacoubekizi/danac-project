# Generated by Django 5.0 on 2024-03-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0017_alter_output_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualreceipt',
            name='shipping_cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='output',
            name='shipping_cost',
            field=models.FloatField(default=0.0),
        ),
    ]
