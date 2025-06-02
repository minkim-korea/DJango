from . import views
from django.urls import path,include

app_name="board"
urlpatterns = [ 
    path('list/', views.list,name="list"), # 게시판
    path('write/', views.write,name="write"), # 글쓰기 
    path('view/<int:bno>/', views.view,name="view"), # 글 상세보기 
    path('update/<int:bno>/', views.update,name="update"), # 글 수정
] 
