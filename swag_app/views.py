from django.shortcuts import render,  get_object_or_404, redirect
from .forms import *
from django.db.models import Q
from .models import *
from .cart import Cart
from django.conf import settings
from django.contrib import messages
# these are built in Django email notifications to the customers for the orders
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

#Marj will handle views

def swag_home(request):
    newest_products = Product.objects.all()[0:8]
    return render(request, 'main.html', {'newest_products': newest_products})

def product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            Cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'The product was added to the cart')
            return redirect('product', product_slug=product_slug)
    else:
        form = AddToCartForm()
    return render(request, 'product.html', {'form': form, 'product': product})

def cart_page(request):
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
                place = form.cleaned_data['place']
                order = checkout(request, first_name, last_name, email, address, zipcode, place, phone, cart.get_total_cost())
                cart.clear()
                notify_customer(order)
                return redirect('success')
    else:
        form = CheckoutForm()
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)
    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')
    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart')
    return render(request, 'cart.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY})

def success(request):
    return render(request, 'success.html')

def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount)
    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], vendor=item['product'].vendor, price=item['product'].price, quantity=item['quantity'])
        order.vendors.add(item['product'].vendor)
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