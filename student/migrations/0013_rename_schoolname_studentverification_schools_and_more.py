# Generated by Django 5.0.6 on 2024-05-14 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_studentverification_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentverification',
            old_name='schoolName',
            new_name='schools',
        ),
        migrations.RenameField(
            model_name='studentverification',
            old_name='studentName',
            new_name='students',
        ),
    ]
