# Generated by Django 2.2.16 on 2020-11-24 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0010_auto_20201122_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 13, 26, 38, 889506, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
