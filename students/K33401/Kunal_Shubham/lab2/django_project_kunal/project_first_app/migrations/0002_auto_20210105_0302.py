# Generated by Django 3.1.4 on 2021-01-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='passport',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
