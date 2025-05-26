from django.urls import path,include
from . import views
app_name=''
urlpatterns = [
    #views.py로 연결을 시키는곳 
    path('',views.index,name="index"), 
]
