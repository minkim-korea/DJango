from django.contrib import admin
from students.models import Student  # 관리자페이지에 등록시키겠다
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','major','grade']


admin.site.register(Student,StudentAdmin)

