# Generated by Django 3.1.3 on 2022-05-07 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0006_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choices',
        ),
        migrations.AddField(
            model_name='submission',
            name='choices',
            field=models.CharField(default='', max_length=255),
        ),
    ]
