# Generated by Django 3.1.7 on 2021-03-10 11:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset_management', '0008_auto_20210309_1213'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userasset',
            unique_together={('asset', 'user')},
        ),
    ]
