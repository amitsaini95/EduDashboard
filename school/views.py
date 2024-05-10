from django.shortcuts import render
from .models import *
# Create your views here.
def SchoolDashboardView(request):
    school=SchoolProfile.objects.get(author=request.user)
    print(school)
    context={'school':school}
    return render(request,"base/schooldashboard.html",context)
