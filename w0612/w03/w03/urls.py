
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('board/',include("board.urls")),
    path('ajaxData/',include("ajaxData.urls")),
]
