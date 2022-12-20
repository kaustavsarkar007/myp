from django.contrib import admin
from django.urls import path

from  home import views


urlpatterns = [

    path('', views.home, name='home'),
    path('', views.footLand, name="footland"), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]