# Generated by Django 3.1.3 on 2020-11-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='address',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='main',
            name='email',
            field=models.EmailField(default='-', max_length=254),
        ),
        migrations.AddField(
            model_name='main',
            name='phone',
            field=models.CharField(default='-', max_length=15),
        ),
    ]
