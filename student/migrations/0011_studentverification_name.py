# Generated by Django 5.0.6 on 2024-05-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_studentverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentverification',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
