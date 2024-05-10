from django import forms
from student.models import StudentProfile
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from school.models import SchoolProfile

   
class UserRegisterForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')
class schoolForm(forms.ModelForm):
    class Meta:
        model=SchoolProfile
        fields=('__all__')
        exclude=('authAdmin','author','slug','publish','status')
    def __init__(self,*args,**kwargs):
        super(schoolForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'


