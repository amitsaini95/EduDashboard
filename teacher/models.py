from django.db import models
from student.models import *
from school.models import *
from django.utils import timezone
import datetime
VERIFY=(
    ('Verify','Verify'),
    ('NotVerify','NotVerify')
)
ATTENDANCE=(
    ('Present','Present'),
    ('Absence','Absence')
)
# Create your models here.
class TeacherProfileModel(models.Model):
    name=models.CharField(max_length=80)
    author=models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    email=models.EmailField()
    phoneNo=models.BigIntegerField()
    schoolName=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE,related_name="teacherSchool")
    profile=models.ImageField(upload_to="teacherProfile",null=True,blank=True)
    address=models.TextField()
    salary=models.IntegerField(blank=True,null=True)
    teacherVerifyBySchool=models.CharField(max_length=20,default='NotVerify',choices=VERIFY)
    city=models.ForeignKey('student.city',on_delete=models.CASCADE,related_name="teacherCity")
    state=models.ForeignKey('student.state',on_delete=models.CASCADE,related_name="teacherState")
    role=models.CharField(max_length=100)
    teachOfClass=models.CharField(max_length=20)
    totalOfStudent=models.ManyToManyField('student.StudentProfileModel',null=True,blank=True)


    def __str__(self):
        return self.name

    
class TeacherAttendanceModel(models.Model):
    teacherName=models.ForeignKey(TeacherProfileModel,on_delete=models.CASCADE)
    schoolName=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE)
    teacherAttend=models.CharField(max_length=10,choices=ATTENDANCE,default="Absence")
    date=models.DateTimeField(default=timezone.now())
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.teacherName.name
