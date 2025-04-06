from django.contrib import admin
from django.contrib.auth.models import User
from .models import School,Teacher,Student
# Register your models here.

admin.site.register(School)
admin.site.register(Teacher)