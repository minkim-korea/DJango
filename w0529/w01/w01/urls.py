from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path ("students/") ## path에 ("주소/") /꼭 붙여야 함!!!
    path('',include('home.urls') ),
    path('students/',include('students.urls') ),
]
