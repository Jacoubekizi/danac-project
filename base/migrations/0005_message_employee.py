# Generated by Django 5.0 on 2024-02-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_chat_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='employee',
            field=models.BooleanField(default=False),
        ),
    ]
