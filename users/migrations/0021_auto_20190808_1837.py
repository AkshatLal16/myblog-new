# Generated by Django 2.2.1 on 2019-08-08 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190808_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 13, 7, 53, 561694, tzinfo=utc)),
        ),
    ]
