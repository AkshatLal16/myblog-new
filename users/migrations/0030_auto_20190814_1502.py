# Generated by Django 2.2.1 on 2019-08-14 09:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20190814_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 9, 32, 38, 933371, tzinfo=utc)),
        ),
    ]