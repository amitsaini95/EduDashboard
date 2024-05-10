from django.shortcuts import render
from .models import *
# Create your views here.
def DashBoardView(request):
   
    return render(request,"base/studentdashboard.html")