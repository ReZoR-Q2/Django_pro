from django.urls import path
from myapp.views import index

urlpatterns = [
     #http://127.0.0.1:8000/
    path('hello/', index)
]
