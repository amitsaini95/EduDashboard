# Generated by Django 5.0.6 on 2024-05-12 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_schoolprofilemodel_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofilemodel',
            name='teacher',
        ),
    ]
