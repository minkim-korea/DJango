from django.urls import path,include
from . import views
app_name='event'
urlpatterns = [
   
    path('list/',views.list,name="list"), # list url -> list 함수호출
]
