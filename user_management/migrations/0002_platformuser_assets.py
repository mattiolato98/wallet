# Generated by Django 3.1.7 on 2021-03-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0007_auto_20210309_1140'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformuser',
            name='assets',
            field=models.ManyToManyField(related_name='user_assets', through='asset_management.UserAsset', to='asset_management.Asset'),
        ),
    ]
