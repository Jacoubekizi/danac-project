# Generated by Django 5.0 on 2024-03-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_remove_customuser_store_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='supplier',
            name='info',
            field=models.TextField(blank=True, default='_', max_length=500, null=True),
        ),
    ]
