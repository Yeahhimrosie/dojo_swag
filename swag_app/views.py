from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#Marj will handle views
def index(request):
    return render(request, 'index.html')

