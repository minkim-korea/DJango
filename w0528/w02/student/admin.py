from django.contrib import admin
from student.models import Student

# admin 관리자 페이지에 Student라는 테이블을 추가
admin.site.register(Student)
