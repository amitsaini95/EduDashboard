from django.urls import path
from .import views
app_name="school"
urlpatterns=[
    path('',views.SchoolDashboardView,name="Dashboard"),
    path('addStudent',views.SchoolStudentView,name="SchoolStudent"),
    path('student',views.StudentDetailsView,name="StudentDetaillist"),
    path('teacher',views.TeacherDetailsView,name="TeacherDetaillist"),
    path('allstudent',views.AllstudentView,name="Allstudentlist"),
    path('studentApproveList',views.studentApproveView,name="studentApprovelist"),
    path('teacherApproveList',views.TeacherApproveView,name="TeacherApprovelist"),
    path('student_Profile/<int:id>',views.EditStudentProfile,name="editstudentprofile"),
    path('teacherProfile/<int:id>',views.EditTeacherView,name="editTeacherProfile"),
    path('addteacher',views.AddTeacherView,name="addteacher"),
    path('teacherList',views.TeacherListView,name="teacherlist"),
    path('attendance',views.StudentTeacherAttendanceView,name="studentAttendanceList"),
    path('studentAttendance',views.StudentAttendanceView,name="STUattendanceList")
]