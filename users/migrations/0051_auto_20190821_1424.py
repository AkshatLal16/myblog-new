# Generated by Django 2.2.1 on 2019-08-21 08:54

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_auto_20190821_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(default=users.models.default_value, related_name='bookmarked_by', to='users.Story'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='claps',
            field=models.ManyToManyField(default=users.models.default_value, related_name='clapped_by', to='users.Story'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(default=users.models.default_value, related_name='followed_by', to='users.Profile'),
        ),
    ]
