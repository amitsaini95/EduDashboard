# Generated by Django 5.0.6 on 2024-05-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_schoolstudent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolstudent',
            old_name='author',
            new_name='schools',
        ),
    ]