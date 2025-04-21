
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/
    path('hello/', views.index)
    
]
