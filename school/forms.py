from django import forms
from student.models import StudentProfileModel
from .models import User,SchoolStudentsModel
from teacher.models import TeacherProfileModel

class studentForm(forms.ModelForm):
    class Meta:
        model=StudentProfileModel
        fields=('name','gender','email','phoneNo','schoolName')
    def __init__(self,*args,**kwargs):
        super(studentForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class EditStudentProfileForm(forms.ModelForm):
    class Meta:
        model=SchoolStudentsModel
        fields=('studentName','email','phoneNo','schoolProf')
    def __init__(self,*args,**kwargs):
        super(EditStudentProfileForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class AddTeacherForm(forms.ModelForm):
    class Meta:
        model=TeacherProfileModel
        fields=('__all__')
        exclude=('authAdmin','author','slug','publish','status','studentList')
    def __init__(self,*args,**kwargs):
        super(AddTeacherForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
       
