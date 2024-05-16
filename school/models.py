from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from Auth.models import User 
from student.models import *
from teacher.models import *
# Create your models here.

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)
class SchoolProfileModel(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True)
    address = models.TextField(null=True, blank=True)
    author = models.ForeignKey('Auth.User', on_delete=models.SET_NULL, related_name='authorSProfile', null=True, blank=True)
    authAdmin = models.OneToOneField('Auth.User',on_delete=models.CASCADE, related_name='authAdminSPM', null=True, blank=True)
    udiseCode=models.CharField(null=True,blank=True,unique=True,max_length=70)
    district=models.CharField(null=True,blank=True,max_length=100)
    block=models.CharField(null=True,blank=True,max_length=100)
    village=models.CharField(null=True,blank=True,max_length=100)
    schoolLogo=models.ImageField(upload_to="schoolLogo",null=True,blank=True)
    pinCode=models.IntegerField(null=True,blank=True)
    schoolCategory=models.CharField(null=True,blank=True,max_length=50)
    principalName=models.CharField(null=True,blank=True,max_length=50)
    principalMobile=models.BigIntegerField(null=True,blank=True)
    principalEmail=models.EmailField(null=True,blank=True,max_length=50)
    spocName=models.CharField(null=True,blank=True,max_length=50)
    spocMobile=models.BigIntegerField(null=True,blank=True)
    spocEmail=models.EmailField(null=True,blank=True,max_length=50)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        return super(SchoolProfileModel,self).save(*args,**kwargs)
    
class SchoolStudentsModel(models.Model):
	author=models.ForeignKey('Auth.User',on_delete=models.CASCADE,null=True,blank=True)
	schoolProf=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE,null=True,blank=True,related_name="studentSchools")
	studentProf=models.ForeignKey('student.StudentProfileModel',on_delete=models.CASCADE,related_name="studentsSS",null=True,blank=True)
	studentName=models.CharField(max_length=60)
	email=models.EmailField()
	phoneNo=models.BigIntegerField(null=True,blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	schoolbystudentVerify=models.BooleanField(null=True,default=False)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	def __str__(self):
		return self.studentName

class schoolBoard(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorSB', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	def __str__(self):
		return self.name or "--Name not Provided--"

	class Meta:
		verbose_name_plural = 'School-School Board'
class schoolNotifications(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	school = models.ForeignKey('school.schoolProfileModel', related_name="schoolSN", on_delete=models.SET_NULL,null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	author = models.ForeignKey('Auth.User', on_delete=models.CASCADE, related_name='authorSN', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
	
	def __str__(self):
		return self.description or '--Name not provided--'
	
	class Meta:
		verbose_name_plural = 'School-School Notifications'


class SchoolTeacherVerification(models.Model):
	teacherName=models.CharField(max_length=100)
	teacherProf=models.ForeignKey('teacher.TeacherProfileModel',on_delete=models.CASCADE)
	schoolProf=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE)
	author=models.ForeignKey('Auth.User',on_delete=models.CASCADE)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

	def __str__(self):
		return self.teacherName or '--Name not provided--'


