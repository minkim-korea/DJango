from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('event/', include('event.urls')),
]
