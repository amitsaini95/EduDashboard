from django.shortcuts import render

# Create your views here.
def SchoolDashboardView(request):
    return render(request,"base/schooldashboard.html")
