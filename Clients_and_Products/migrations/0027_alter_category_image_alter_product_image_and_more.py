# Generated by Django 5.0 on 2024-03-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients_and_Products', '0026_alter_client_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/account.jpg', null=True, upload_to='images/categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/account.jpg', null=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='image',
            field=models.ImageField(default='images/account.jpg', null=True, upload_to='images/product_types'),
        ),
    ]
