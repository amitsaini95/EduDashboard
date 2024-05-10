from django.db import models
from django.contrib.auth.models import AbstractUser
ROLES = (('student', 'Student'), ('teacher', 'Teacher'),('staff','staff'),('school','school'),('admin','admin'))
# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=60)
    types=models.CharField(max_length=50,choices=ROLES,default="admin")

    def __str__(self):
        return self.username
