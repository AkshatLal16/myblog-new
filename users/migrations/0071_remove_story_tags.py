# Generated by Django 2.2.1 on 2019-08-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0070_story_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='tags',
        ),
    ]