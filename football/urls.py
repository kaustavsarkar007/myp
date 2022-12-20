from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.footHome, name="foothome"),   
      
    path('<str:slug>', views.footPost, name="footpost"),
]