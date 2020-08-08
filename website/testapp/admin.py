from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employee #Name
# Register your models here.
admin.site.register(Employee)
from .models import Student
#admin.site.register(Name)


admin.site.register(Student)