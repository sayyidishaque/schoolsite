from django.contrib import admin
from . models import Registration, MaterialProvide, Department, Courses, Purpose
# Register your models here.
admin.site.register(Registration)
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(MaterialProvide)
admin.site.register(Purpose)
