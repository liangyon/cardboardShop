# Generated by Django 4.1.7 on 2023-02-23 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carddatabase', '0002_remove_cardinfo_frametype_remove_cardinfo_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardinfo',
            old_name='frame_type',
            new_name='frameType',
        ),
        migrations.RenameField(
            model_name='cardinfo',
            old_name='card_type',
            new_name='type',
        ),
    ]