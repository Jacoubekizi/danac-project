# Generated by Django 5.0 on 2024-02-28 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Fund', '0003_registry_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='registry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Fund.registry'),
        ),
    ]