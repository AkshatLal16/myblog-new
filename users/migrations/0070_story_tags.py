# Generated by Django 2.2.1 on 2019-08-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0069_auto_20190828_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_by', to='users.Genre'),
        ),
    ]
