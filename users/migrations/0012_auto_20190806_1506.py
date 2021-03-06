# Generated by Django 2.2.1 on 2019-08-06 09:36

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190803_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 6, 9, 36, 47, 995325, tzinfo=utc)),
        ),
    ]
