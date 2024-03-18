# Generated by Django 5.0 on 2024-02-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_returnedgoodsclient_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damagedproduct',
            name='date',
        ),
        migrations.CreateModel(
            name='DamagedPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('goods', models.ManyToManyField(to='base.damagedproduct')),
            ],
        ),
    ]