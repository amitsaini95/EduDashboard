# Generated by Django 5.0.6 on 2024-05-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofilemodel',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='teacherProfile'),
        ),
    ]