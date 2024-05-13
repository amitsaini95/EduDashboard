from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import studentForm,EditStudentProfileForm
from teacher.forms import AddTeacherForm,EditTeacherForm
from student.models import StudentProfileModel,StudentAttendance
from teacher.models import TeacherProfileModel
# Create your views here.
def SchoolDashboardView(request):
    school=SchoolStudentsModel.objects.filter(schoolProf__author=request.user)
    teacherdata=TeacherProfileModel.objects.filter(schoolName__name=request.user)
    StuAttend=StudentAttendance.objects.filter(school__author=request.user,status='published')
    context={'school':school,'TotalTeacher':teacherdata,'StudAttend':StuAttend}
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
            schoolstudentdata=SchoolStudentsModel.objects.create(studentProf=user)
            schoolstudentdata.schoolProf=user.schoolName
            schoolstudentdata.studentName=user.name
            schoolstudentdata.email=user.email
            schoolstudentdata.phoneNo=user.phoneNo
            schoolstudentdata.save()
            return redirect('school:Dashboard')
    else:
        form=studentForm()
    context={
        'form':form
    }
    return render(request,"base/register.html",context)
def AddTeacherView(request):
    if request.method == "POST":
        form=AddTeacherForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            userdata=User.objects.create(username=user.name,types="teacher")
            userdata.set_password(user.name[:3]+'@123')
            userdata.save()
            user.author=userdata
            
            user.save()
        
            
    else:
        form=AddTeacherForm()
    context={
        'form':form
    }
    return render(request,"base/addteacher.html",context)
   
def AllstudentView(request):
    schoolStudnet=SchoolStudentsModel.objects.filter(schoolProf__author=request.user).order_by('-id')
    context={
        'schoolStudent':schoolStudnet
    }
    return render(request,'base/allstudent.html',context)
def EditStudentProfile(request,id):
    instance=SchoolStudentsModel.objects.get(id=id)
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
def TeacherListView(request):
    teacherdata=TeacherProfileModel.objects.filter(schoolName__author=request.user).order_by('-id')
    context={'teachers':teacherdata}
    return render(request,"base/allteacher.html",context)
def EditTeacherView(request,id):
    instance=TeacherProfileModel.objects.get(id=id)
    if request.method == "POST":
        form=EditTeacherForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=EditTeacherForm(instance=instance)
    context={
        'form':form
    }
    return render(request,"base/editteacher.html",context)
def StudentAttendanceView(request):
    stuData=StudentAttendance.objects.filter(school__author=request.user)
    context={
      'stuData':stuData
    }
    return render(request,"base/studentattendance.html",context)

