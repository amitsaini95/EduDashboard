from django.db import models
from student.models import *
from school.models import *


# Create your models here.
class TeacherProfileModel(models.Model):
    name=models.CharField(max_length=80)
    author=models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    email=models.EmailField()
    phoneNo=models.BigIntegerField()
    schoolName=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE,related_name="teacherSchool")
    profile=models.ImageField(upload_to="teacherProfile")
    address=models.TextField()
    city=models.ForeignKey('student.city',on_delete=models.CASCADE,related_name="teacherCity")
    state=models.ForeignKey('student.state',on_delete=models.CASCADE,related_name="teacherState")
    role=models.CharField(max_length=100)
    teachOfClass=models.CharField(max_length=20)
    totalOfStudent=models.ManyToManyField('student.StudentProfileModel',null=True,blank=True)
    def __str__(self):
        return self.name

    