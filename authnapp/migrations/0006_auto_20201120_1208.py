# Generated by Django 2.2.16 on 2020-11-20 12:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0005_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 12, 8, 28, 243812, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
