# Generated by Django 5.0.6 on 2024-05-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_rename_publish_studentattendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='stuAttend',
            field=models.CharField(blank=True, choices=[('Present', 'Present'), ('Absence', 'Absence')], default='Absence', max_length=10, null=True),
        ),
    ]