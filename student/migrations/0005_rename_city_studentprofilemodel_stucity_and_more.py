# Generated by Django 5.0.6 on 2024-05-12 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentprofilemodel_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofilemodel',
            old_name='city',
            new_name='stuCity',
        ),
        migrations.RenameField(
            model_name='studentprofilemodel',
            old_name='state',
            new_name='stuState',
        ),
    ]
