# Generated by Django 2.2.16 on 2020-11-24 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0014_auto_20201124_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 13, 56, 48, 623074, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
