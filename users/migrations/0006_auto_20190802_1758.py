# Generated by Django 2.2.1 on 2019-08-02 12:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190802_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 2, 12, 28, 12, 244121, tzinfo=utc)),
        ),
    ]
