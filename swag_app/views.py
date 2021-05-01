from django.shortcuts import render,  get_object_or_404, redirect
from django.db.models import Q
from .forms import *
from .models import *
from .cart import Cart #we are importing the methods in cart.py 
from django.conf import settings
from django.contrib import messages

# these are built in Django email notifications to the customers for the orders

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.


#Marj will handle views

def swag_home(request):
    context = {
        'all_products': Product.objects.all(), 
    }
    return render(request, 'main.html', context)

def product_page(request, product_slug,):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity-1, update_quantity=True)
            messages.success(request, 'The product was added to the cart')
            return redirect('products', product_slug=product_slug)
    else:
        form = AddToCartForm()
    return render(request, 'product.html', { 'form': form, 'product': product })

def cart_page(request):
    cart = Cart(request)
    if request.method == 'GET':
        remove_from_cart = request.GET.get('remove_from_cart', '')
        change_quantity = request.GET.get('change_quantity', '')
        quantity = request.GET.get('quantity', 0)
        if remove_from_cart:
            cart.remove(remove_from_cart)
            cart.save()
            return redirect('cart')
        if change_quantity:
            cart.add(change_quantity, quantity, True)
            cart.save()
            return redirect('cart')
    return render(request, 'cart.html')

def checkout_page(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                state = form.cleaned_data['state']
                order = checkout(request, first_name, last_name, email, address, zipcode, state, phone, cart.get_total_cost())
                cart.clear()
                notify_customer(order)
                messages.success(request, 'Thanks for ordering!')
                return redirect('dojoswag/checkoutpage')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form })

def success(request):
    return render(request, 'success.html')

def checkout(request, first_name, last_name, email, address, zipcode, state, phone, amount):
    order = Order.objects.create(
        first_name=first_name, 
        last_name=last_name, 
        email=email, 
        address=address, 
        zipcode=zipcode, state=state, 
        phone=phone, 
        paid_amount=amount)
    for item in Cart(request):
        OrderItem.objects.create(
            order=order, 
            product=item['product'], 
            price=item['product'].price, 
            quantity=item['quantity']
            )
        order.add(item['product'])
    return order

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM
    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
