# Generated by Django 2.2.1 on 2019-08-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0055_auto_20190826_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='response_claps',
            field=models.ManyToManyField(blank=True, related_name='resonse_claps_by', to='users.Responses'),
        ),
    ]
