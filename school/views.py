from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import studentForm,EditStudentProfileForm
from student.models import StudentProfile
# Create your views here.
def SchoolDashboardView(request):
    school=SchoolStudent.objects.filter(schools__author=request.user)
    context={'school':school}
    return render(request,"base/schooldashboard.html",context)

def SchoolStudentView(request):
    if request.method == "POST":
        form=studentForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            userdata=User.objects.create(username=user.name,types="student")
            userdata.set_password(user.name[:3]+'@123')
            userdata.save()
            user.author=userdata
            user.authAdmin=userdata
            user.save()
            schoolstudentdata=SchoolStudent.objects.create(student=user)
            schoolstudentdata.schools=user.schoolName
            schoolstudentdata.studentName=user.name
            schoolstudentdata.save()
            return redirect('school:Dashboard')
    else:
        form=studentForm()
    context={
        'form':form
    }
    return render(request,"base/register.html",context)
   
def AllstudentView(request):
    schoolStudnet=SchoolStudent.objects.filter(schools__author=request.user).order_by('-id')
    context={
        'schoolStudent':schoolStudnet
    }
    return render(request,'base/allstudent.html',context)
def EditStudentProfile(request,id):
    instance=SchoolStudent.objects.get(id=id)
    if request.method == "POST":
        form=EditStudentProfileForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('school:Allstudentlist')
    else:
        form=EditStudentProfileForm(instance=instance)
    context={
        'form':form
    }
    return render(request,"base/editstudentProfile.html",context)