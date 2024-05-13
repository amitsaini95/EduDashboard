from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(StudentProfileModel)
admin.site.register(state)
admin.site.register(city)
admin.site.register(StudentClass)
admin.site.register(StudentAttendance)
admin.site.register(StudentVerification)

