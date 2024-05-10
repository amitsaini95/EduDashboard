from django.shortcuts import render,redirect
from .models import *
from .forms import studentForm
# Create your views here.
def SchoolDashboardView(request):
    school=SchoolProfile.objects.get(author=request.user)
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
            return redirect('school:Dashboard')
    else:
        form=studentForm()
    context={
        'form':form
    }
    return render(request,"base/register.html",context)
   
