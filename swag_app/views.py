from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#Marj will handle views
def swag_home(request):
    context = {
        'product_images':Product.objects.all(), 
    }

    return render(request, 'main.html', context)

