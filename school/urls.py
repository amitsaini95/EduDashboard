from django.urls import path
from .import views
app_name="school"
urlpatterns=[
    path('',views.SchoolDashboardView,name="Dashboard"),
    path('addStudent',views.SchoolStudentView,name="SchoolStudent")
]