from django.urls import path,include
from . import views

app_name='studentsapp'
urlpatterns = [
    path('list/',views.list,name='list'), # 학생전체 리스트 
    path('view/',views.view,name='view'),  # 학생상세 페이지 
    path('write/',views.write,name='write'), # 학생입력페이지
    path('delete/',views.delete,name='delete'), #학생삭제페이지
]


