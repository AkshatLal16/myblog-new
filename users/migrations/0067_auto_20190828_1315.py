# Generated by Django 2.2.1 on 2019-08-28 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_auto_20190828_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='category2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.GenreCategory'),
        ),
    ]
