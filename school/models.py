from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from Auth.models import User
# Create your models here.

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)
class SchoolProfile(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True)
    address = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authorSProfile', null=True, blank=True)
    authAdmin = models.OneToOneField(User,on_delete=models.CASCADE, related_name='authAdminSPM', null=True, blank=True)
    udiseCode=models.CharField(null=True,blank=True,unique=True,max_length=70)
    district=models.CharField(null=True,blank=True,max_length=100)
    block=models.CharField(null=True,blank=True,max_length=100)
    village=models.CharField(null=True,blank=True,max_length=100)
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
        return super(SchoolProfile,self).save(*args,**kwargs)
