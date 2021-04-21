from django.contrib import admin
from django.urls import path
from . import views

#Roy will handle urls

urlpatterns = [
    path('', views.index),
    path('/dojoswag', views.swag_home)
]
