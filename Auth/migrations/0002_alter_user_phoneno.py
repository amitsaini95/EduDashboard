# Generated by Django 5.0.6 on 2024-05-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]