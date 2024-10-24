from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ben10', views.ben10, name='ben10'),
    path('tomandjerry', views.tom, name='tom'),
]