# Generated by Django 5.0 on 2024-02-06 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Products', '0001_initial'),
        ('Human_Resources', '0001_initial'),
        ('Receipts', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incoming',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.supplier'),
        ),
        migrations.AddField(
            model_name='incoming_product',
            name='incoming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.incoming'),
        ),
        migrations.AddField(
            model_name='incoming_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='products',
            field=models.ManyToManyField(through='Receipts.Incoming_Product', to='Clients_and_Products.product'),
        ),
        migrations.AddField(
            model_name='manualreceipt',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.client'),
        ),
        migrations.AddField(
            model_name='manualreceipt',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee'),
        ),
        migrations.AddField(
            model_name='manualreceipt_products',
            name='manualreceipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.manualreceipt'),
        ),
        migrations.AddField(
            model_name='manualreceipt_products',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product'),
        ),
        migrations.AddField(
            model_name='manualreceipt',
            name='products',
            field=models.ManyToManyField(through='Receipts.ManualReceipt_Products', to='Clients_and_Products.product'),
        ),
        migrations.AddField(
            model_name='output',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.client'),
        ),
        migrations.AddField(
            model_name='output',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Human_Resources.employee'),
        ),
        migrations.AddField(
            model_name='output_products',
            name='output',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.output'),
        ),
        migrations.AddField(
            model_name='output_products',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Products.product'),
        ),
        migrations.AddField(
            model_name='output',
            name='products',
            field=models.ManyToManyField(through='Receipts.Output_Products', to='Clients_and_Products.product'),
        ),
    ]
