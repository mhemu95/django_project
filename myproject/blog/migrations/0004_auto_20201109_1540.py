# Generated by Django 3.1.3 on 2020-11-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201109_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='-', max_length=10),
        ),
    ]
