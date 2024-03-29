# Generated by Django 5.0 on 2024-02-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='store_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='town',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='work_hours',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
