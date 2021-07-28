from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.home, name='Home Page' ),
    path('<id>/', views.getdata, name='Get Request Page' ),
]
