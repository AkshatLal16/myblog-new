# Generated by Django 2.2.1 on 2019-08-28 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0068_remove_genre_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='category2',
            new_name='category',
        ),
    ]
