from django import forms
from student.models import StudentProfileModel
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from school.models import SchoolProfileModel

   
class UserRegisterForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')
class schoolForm(forms.ModelForm):
    class Meta:
        model=SchoolProfileModel
        fields=('__all__')
        exclude=('authAdmin','author','slug','publish','status','studentList')
    def __init__(self,*args,**kwargs):
        super(schoolForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'


