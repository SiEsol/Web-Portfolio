# Generated by Django 5.0.7 on 2024-07-24 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_item_subtitile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='subtitile',
            new_name='subtitle',
        ),
    ]