from django.urls import path,include
from . import views

app_name="students"
urlpatterns = [
    
    path('write/',views.write,name="write"),
    path('result/',views.result,name="result"),
]
