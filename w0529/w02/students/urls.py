
from . import views
from django.urls import path,include

app_name="students"
urlpatterns = [
    path('list/',views.list,name="list"),  
    path('write/',views.write,name="write"),  
    path('writeOk/',views.writeOk,name="writeOk"),  
    path('writeOk/',views.writeOk,name="writeOk"),  
    path('writeOk/',views.writeOk,name="writeOk"),  
    path('update/<int:no>/',views.update,name="update"), #학생정보수정페이지 열기 
    path('updateOk/',views.updateOk,name="updateOk"), # 학생정보 수정한거 저장
    path('delete/<int:no>/',views.delete,name="delete"), # 학생정보 삭제
    path('view/<int:no>/',views.view,name="view"), # 학생정보 삭제

]
