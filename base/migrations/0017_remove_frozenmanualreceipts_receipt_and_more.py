# Generated by Django 5.0 on 2024-02-22 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_frozenincomingreceipts_frozenoutputreceipts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frozenmanualreceipts',
            name='receipt',
        ),
        migrations.RemoveField(
            model_name='frozenoutputreceipts',
            name='receipt',
        ),
        migrations.DeleteModel(
            name='FrozenIncomingReceipts',
        ),
        migrations.DeleteModel(
            name='FrozenManualReceipts',
        ),
        migrations.DeleteModel(
            name='FrozenOutputReceipts',
        ),
    ]
