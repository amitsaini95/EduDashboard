from django.urls import path
from .import views
app_name="school"
urlpatterns=[
    path('',views.SchoolDashboardView,name="Dashboard"),
    path('addStudent',views.SchoolStudentView,name="SchoolStudent"),
    path('allstudent',views.AllstudentView,name="Allstudentlist"),
    path('student_Profile/<int:id>',views.EditStudentProfile,name="editstudentprofile"),
    path('addteacher',views.AddTeacherView,name="addteacher"),
    path('teacherList',views.TeacherListView,name="teacherlist")
]