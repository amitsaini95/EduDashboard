# Generated by Django 5.0.6 on 2024-05-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_studentclass_studentattendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]