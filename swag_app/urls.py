from django.contrib import admin
from django.urls import path
from . import views

#Roy will handle urls

urlpatterns = [
    path('dojoswag', views.swag_home),
    path('dojoswag/checkoutpage', views.checkout_page),
    path('dojoswag/cartpage', views.cart_page),
    path('dojoswag/productpage', views.product_page),
    path('dojoswag/addcart', views.add_to_cart),
    path('dojoswag/deletecart', views.delete_from_cart),
    path('dojoswag/checkout', views.checkout),
    path('dojoswag/submitorder', views.submit_order),
]
