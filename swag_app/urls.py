from django.contrib import admin
from django.urls import path
from . import views
####
# from django.conf import settings
# from django.conf.urls.static import static

#Roy will handle urls

urlpatterns = [
    path('', views.swag_home),
    path('dojoswag/checkoutpage', views.checkout_page),
    path('dojoswag/cartpage', views.cart_page),
    path('dojoswag/productpage', views.product_page, name='product'),
    # path('dojoswag/deletecart', views.delete_from_cart),
    path('dojoswag/checkout', views.checkout),
    # path('dojoswag/submitorder', views.submit_order),
    path('success', views.success),
]

