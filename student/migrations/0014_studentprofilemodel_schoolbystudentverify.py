# Generated by Django 5.0.6 on 2024-05-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_rename_schoolname_studentverification_schools_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofilemodel',
            name='schoolbystudentVerify',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
