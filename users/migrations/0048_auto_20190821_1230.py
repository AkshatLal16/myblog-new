# Generated by Django 2.2.1 on 2019-08-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_auto_20190821_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='claps',
        ),
        migrations.AddField(
            model_name='profile',
            name='claps',
            field=models.ManyToManyField(related_name='clapped_by', to='users.Story'),
        ),
    ]
