from django.contrib import admin
from django.urls import path
from django.conf import settings
from myapp import views
urlpatterns = [
    
    path('',views.d,name='d'),
]