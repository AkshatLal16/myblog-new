# Generated by Django 2.2.1 on 2019-08-14 09:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0026_auto_20190813_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 9, 19, 33, 292612, tzinfo=utc)),
        ),
    ]
