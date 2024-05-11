from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import studentForm
from student.models import StudentProfile
# Create your views here.
def SchoolDashboardView(request):
    school=SchoolProfile.objects.get(author=request.user)
    totalstudent=school.studentList.all().count()
    
    context={'school':school,'totalstudent':totalstudent}
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
            user.studentList.add(userdata)
            user.authAdmin=userdata
            user.save()
            return redirect('school:Dashboard')
    else:
        form=studentForm()
    context={
        'form':form
    }
    return render(request,"base/register.html",context)
   
def AllstudentView(request):
    if request.user.types=="school":
        print(request.user)
        schoolStudnet=SchoolStudent.objects.filter(schools__author=request.user).order_by('-id')
        print(schoolStudnet)
    
        context={
            'schoolStudent':schoolStudnet
        }

        return render(request,'base/allstudent.html',context)
    else:
        return HttpResponse("not data")
