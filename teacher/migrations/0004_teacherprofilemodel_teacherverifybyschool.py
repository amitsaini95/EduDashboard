# Generated by Django 5.0.6 on 2024-05-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacherprofilemodel_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofilemodel',
            name='teacherVerifyBySchool',
            field=models.BooleanField(default=False, max_length=20),
        ),
    ]