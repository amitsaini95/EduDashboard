from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegisterForm,schoolForm
from django.contrib.auth import authenticate,login,logout
from Auth.models import User
from student.views import *
from school.views import *

# Create your views here.
def StudentRegisterView(request):
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
            return redirect('Auth:dashboard')
    else:
        form=studentForm()
    context={
        'form':form
    }
    return render(request,"base/register.html",context)
def SchoolRegisterView(request):
    if request.method == "POST":
        form=schoolForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            userdata=User.objects.create(username=user.name,types="school")
            userdata.set_password(user.name[:3]+'@123')
            userdata.save()
            user.author=userdata
            user.authAdmin=userdata
            user.save()
            return redirect('Auth:Login')
    else:
        form=schoolForm()
    context={
        'form':form
    }
    return render(request,"base/schoolregister.html",context)
def LoginView(request):
    if request.method == "POST":
        form=UserRegisterForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if request.user.types=="student":
                    return redirect('student:Dashboard')
                elif request.user.types=="school":
                    return redirect('school:Dashboard')
    else:
        form=UserRegisterForm()
    context={
        'form':form
    }
    return render(request,"base/login.html",context)

  