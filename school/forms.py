from django import forms
from student.models import StudentProfile
from .models import User,SchoolStudent

class studentForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=('name','gender','phoneNo','schoolName')
    def __init__(self,*args,**kwargs):
        super(studentForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class EditStudentProfileForm(forms.ModelForm):
    class Meta:
        model=SchoolStudent
        fields=('studentName','email','phoneNo','schools')
    def __init__(self,*args,**kwargs):
        super(EditStudentProfileForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
       
