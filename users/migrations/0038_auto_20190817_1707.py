# Generated by Django 2.2.1 on 2019-08-17 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20190817_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 17, 11, 37, 33, 802565, tzinfo=utc)),
        ),
    ]
