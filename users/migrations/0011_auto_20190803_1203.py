# Generated by Django 2.2.1 on 2019-08-03 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190802_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 3, 6, 33, 8, 813186, tzinfo=utc)),
        ),
    ]
