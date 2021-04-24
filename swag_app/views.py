from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#Marj will handle views
def swag_home(request):
    return render(request, 'main.html')

