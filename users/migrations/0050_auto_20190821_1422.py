# Generated by Django 2.2.1 on 2019-08-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20190821_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(default=None, related_name='bookmarked_by', to='users.Story'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='claps',
            field=models.ManyToManyField(default=None, related_name='clapped_by', to='users.Story'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(default=None, related_name='followed_by', to='users.Profile'),
        ),
    ]
