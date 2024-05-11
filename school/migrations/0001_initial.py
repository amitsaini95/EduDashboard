# Generated by Django 5.0.6 on 2024-05-11 05:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('udiseCode', models.CharField(blank=True, max_length=70, null=True, unique=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('block', models.CharField(blank=True, max_length=100, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('schoolLogo', models.ImageField(blank=True, null=True, upload_to='schoolLogo')),
                ('pinCode', models.IntegerField(blank=True, null=True)),
                ('schoolCategory', models.CharField(blank=True, max_length=50, null=True)),
                ('principalName', models.CharField(blank=True, max_length=50, null=True)),
                ('principalMobile', models.BigIntegerField(blank=True, null=True)),
                ('principalEmail', models.EmailField(blank=True, max_length=50, null=True)),
                ('spocName', models.CharField(blank=True, max_length=50, null=True)),
                ('spocMobile', models.BigIntegerField(blank=True, null=True)),
                ('spocEmail', models.EmailField(blank=True, max_length=50, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('authAdmin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authAdminSPM', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorSProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
