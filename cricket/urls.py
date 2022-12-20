from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cricHome, name="crichome"),   
    path('<str:slug>', views.cricPost, name="cricpost"),   
    
]