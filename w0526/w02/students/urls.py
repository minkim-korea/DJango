from django.urls import path,include
from . import views
app_name='students'
urlpatterns = [
    #views.py로 연결을 시키는곳 
    path('list/',views.list,name="list"),
  
]
