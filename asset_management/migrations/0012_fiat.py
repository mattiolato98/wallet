# Generated by Django 3.1.7 on 2021-03-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0011_auto_20210313_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sign', models.CharField(max_length=5)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
    ]
