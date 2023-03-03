# Generated by Django 4.1.7 on 2023-03-03 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carddatabase', '0004_cardinfo_card_images_cardinfo_card_prices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardinfo',
            name='sanitized_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='updated_date',
            field=models.DateTimeField(default=datetime.date(1955, 12, 25)),
        ),
    ]
