from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('arts', views.arts),
    path('ukr', views.index_ua),
    path('deu', views.index_de)
]