from django import forms
from student.models import StudentProfile
from .models import User
class studentForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=('__all__')
        exclude=('authAdmin','author','publish','status')
    def __init__(self,*args,**kwargs):
        super(studentForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'