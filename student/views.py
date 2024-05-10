from django.shortcuts import render

# Create your views here.
def DashBoardView(request):
    return render(request,"base/studentdashboard.html")