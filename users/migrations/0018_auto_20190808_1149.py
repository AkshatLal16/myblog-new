# Generated by Django 2.2.1 on 2019-08-08 06:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190807_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 6, 19, 14, 652255, tzinfo=utc)),
        ),
    ]