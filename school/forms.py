from django import forms
from student.models import StudentProfileModel
from .models import User,SchoolStudentsModel

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


       
