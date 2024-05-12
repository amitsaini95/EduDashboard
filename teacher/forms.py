from django import forms
from .models import *
class AddTeacherForm(forms.ModelForm):
    class Meta:
        model=TeacherProfileModel
        fields=('__all__')

    def __init__(self,*args,**kwargs):
        super(AddTeacherForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
class EditTeacherForm(forms.ModelForm):
    class Meta:
        model=TeacherProfileModel
        fields=('__all__')
    def __init__(self,*args,**kwargs):
        super(EditTeacherForm,self).__init__(*args,**kwargs)
        for fieldName,fields in self.fields.items():
            fields.widget.attrs['class']='form-control'
    
    
    
     
    