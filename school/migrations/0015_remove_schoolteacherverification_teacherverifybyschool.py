# Generated by Django 5.0.6 on 2024-05-16 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_schoolteacherverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolteacherverification',
            name='teacherVerifyBySchool',
        ),
    ]
