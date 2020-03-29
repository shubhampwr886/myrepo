
from django.contrib import admin
from django.urls import path
from . import welcome

urlpatterns = [
    path('', welcome.page1),
    path('admin/', admin.site.urls),
    path('external',welcome.external)
 
]
