# Generated by Django 2.2.1 on 2019-08-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20190827_1634'),
        ('blog', '0004_auto_20190827_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagedata',
            name='BACKUP_HOMEPAGE_STORY',
            field=models.ManyToManyField(blank=True, related_name='bkp', to='users.Story'),
        ),
    ]
