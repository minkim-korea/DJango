from . import views
from django.urls import path,include

app_name="students"
urlpatterns = [
    path('list/',views.list,name="list"),
    path('write/',views.write,name="write"),
    path('view/',views.view,name="view"),
    path('update/<str:name>/',views.update,name="update"),  
    path('delete/<str:name>/',views.delete,name="delete"),  
]
