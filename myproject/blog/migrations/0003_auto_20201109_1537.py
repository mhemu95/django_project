# Generated by Django 3.1.3 on 2020-11-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201109_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.CharField(default='-', max_length=8),
        ),
    ]
