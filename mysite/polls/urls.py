from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('index', views.index, name="polls"),
    path('sample', views.sample, name='sample'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]