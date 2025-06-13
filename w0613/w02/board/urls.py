from django.urls import path,include
from . import views

app_name="board"
urlpatterns = [

    path('notice/',views.notice,name="notice"),
    path('notice_view/',views.notice_view,name="notice_view"),
  
]

