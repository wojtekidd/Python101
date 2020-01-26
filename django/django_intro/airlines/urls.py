from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('/upload_flights', views.upload_flights),
    path('/upload_passengers', views.upload_passengers),
]