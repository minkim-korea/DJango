
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # students app >urls.py 로연결 
    path('event/', include('event.urls')), # students app >urls.py 로연결 
    path('stuscore/', include('stuscore.urls')), # students app >urls.py 로연결 
    path('', include('home.urls')), # students app >urls.py 로연결 
]
