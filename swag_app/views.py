from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#Marj will handle views
def swag_home(request):
    context = {
        'all_products':Product.objects.all(), 
    }

    return render(request, 'main.html', context)

def product_page(request, product_id):
    context = {
        'one_product': Product.objects.get(id=product_id),
    }
    return render(request, 'product.html', context)