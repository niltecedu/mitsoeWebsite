from django.urls import path
from django.shortcuts import render

from . import views

app_name='home'
urlpatterns = [
    path('',views.home,name='home'),
]
