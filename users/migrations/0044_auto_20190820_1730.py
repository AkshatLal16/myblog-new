# Generated by Django 2.2.1 on 2019-08-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20190820_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='users.Profile'),
        ),
    ]
