# Generated by Django 2.2.1 on 2019-08-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_story_claps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='claps',
        ),
        migrations.AddField(
            model_name='story',
            name='claps',
            field=models.ManyToManyField(related_name='clapped_by', to='users.Story'),
        ),
    ]
