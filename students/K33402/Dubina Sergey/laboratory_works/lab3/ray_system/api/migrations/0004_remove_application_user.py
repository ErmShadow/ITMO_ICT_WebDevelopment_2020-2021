# Generated by Django 3.1.1 on 2020-12-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201207_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
    ]
