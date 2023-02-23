# Generated by Django 4.1.7 on 2023-02-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carddatabase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardinfo',
            name='frameType',
        ),
        migrations.RemoveField(
            model_name='cardinfo',
            name='type',
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='archetype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='card_type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='frame_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='linkmarkers',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='linkval',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='attack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='attribute',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='defense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='race',
            field=models.CharField(max_length=50),
        ),
    ]
