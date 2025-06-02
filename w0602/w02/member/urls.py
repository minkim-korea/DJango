from . import views
from django.urls import path,include

app_name="member"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('join01/', views.join01,name="join01"),  # 동의페이지
    path('join02/', views.join02,name="join02"),  # 회원가입페이지 
    path('join03/', views.join03,name="join03"),  # 회원가입페이지 
    path('logout/', views.logout,name="logout"),  # 회원가입페이지 
]
