# Generated by Django 5.0.6 on 2024-05-14 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacherprofilemodel_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofilemodel',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]