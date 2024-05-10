from django.db import models
from Auth.models import User
from school.models import SchoolProfile
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
class StudentProfile(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="StudentUsers",null=True)
    name=models.CharField(max_length=100)
    phoneNo=models.BigIntegerField()
    address=models.TextField()
    email=models.EmailField()
    pinCode=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=30,choices=GENDER_CHOICES)
    profile=models.ImageField(upload_to="studentImage",blank=True,null=True)
    category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    authAdmin=models.OneToOneField(User,on_delete=models.CASCADE,related_name="StudentAdmin",null=True)
    schoolName=models.ForeignKey('school.SchoolProfile',on_delete=models.CASCADE,related_name="studentschols")
    fatherName = models.CharField(null=True, blank=True,max_length=50)
    motherName = models.CharField(null=True, blank=True,max_length=50)
    totalFamilyIncome = models.PositiveIntegerField(null=True, blank=True)
    totalFamilyMember=models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
  