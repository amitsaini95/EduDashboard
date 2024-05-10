from django.urls import path
from .import views
app_name="Auth"
urlpatterns=[
    path('schoolRegister',views.SchoolRegisterView,name="School"),
    path('login',views.LoginView,name="Login"),
]