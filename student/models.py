from django.db import models
from Auth.models import User
from school.models import *
from teacher.models import *
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)

CATEGORY_CHOICES = (
    ('General', 'General'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('OBC', 'OBC'),
    ('Others', 'Others'),

)
STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)
  

class StudentClass(models.Model):
	name=models.CharField(max_length=20)
	slug=models.SlugField(max_length=20,blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	def __str__(self):
		return self.name


class state(models.Model):
	name = models.TextField()
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(null=True, blank=True)
	author = models.ForeignKey('Auth.User', on_delete=models.SET_NULL, null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Student-State'
	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		return super(state,self).save(*args,**kwargs)
    
class city(models.Model):
	name = models.TextField()
	slug = models.SlugField(max_length=250, unique=True)
	author = models.ForeignKey('Auth.User', on_delete=models.SET_NULL, null=True, blank=True)
	cityState = models.ForeignKey(state, related_name='cityStateC', on_delete=models.SET_NULL, blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Student-City'
	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		return super(city,self).save(*args,**kwargs)
  
      
class StudentProfileModel(models.Model):
	author=models.ForeignKey('Auth.User',on_delete=models.CASCADE,related_name="StudentUsers",null=True)
	name=models.CharField(max_length=100)
	phoneNo=models.BigIntegerField()
	address=models.TextField()
	email=models.EmailField()
	pinCode=models.IntegerField(null=True,blank=True)
	dob=models.DateField(null=True,blank=True)
	stuState=models.ForeignKey('student.state',on_delete=models.CASCADE,related_name="StuState",null=True,blank=True)
	stuCity=models.ForeignKey('student.city',on_delete=models.CASCADE,related_name="StuCity",null=True,blank=True)
	gender=models.CharField(max_length=30,choices=GENDER_CHOICES)
	profile=models.ImageField(upload_to="studentImage",blank=True,null=True)
	category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)
	authAdmin=models.OneToOneField(User,on_delete=models.CASCADE,related_name="StudentAdmin",null=True)
	schoolName=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE,related_name="studentschols",null=True,blank=True)
	fatherName = models.CharField(null=True, blank=True,max_length=50)
	motherName = models.CharField(null=True, blank=True,max_length=50)
	totalFamilyIncome = models.PositiveIntegerField(null=True, blank=True)
	totalFamilyMember=models.IntegerField(null=True,blank=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name
class StudentAttendance(models.Model):
	school=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE)
	studentClass=models.ForeignKey('student.StudentClass',on_delete=models.CASCADE)
	studentName=models.ForeignKey('student.StudentProfileModel',on_delete=models.CASCADE)
	teacher=models.ForeignKey('teacher.TeacherProfileModel',on_delete=models.CASCADE)
	section=models.CharField(max_length=10)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.studentName.name

class StudentVerification(models.Model):
	students=models.ForeignKey('student.StudentProfileModel',on_delete=models.CASCADE,null=True,blank=True)
	schools=models.ForeignKey('school.SchoolProfileModel',on_delete=models.CASCADE,null=True,blank=True)
	author=models.ForeignKey('Auth.User',on_delete=models.CASCADE,null=True,blank=True)
	name=models.CharField(max_length=60)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name