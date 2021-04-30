from django.contrib import admin
from django.urls import path
from . import views
####
# from django.conf import settings
# from django.conf.urls.static import static

#Roy will handle urls

urlpatterns = [
    path('', views.swag_home, name="main"),
    path('dojoswag/checkoutpage', views.checkout_page, name="checkout"),
    path('dojoswag/cartpage', views.cart_page, name="cart"),
    path('<slug:product_slug>', views.product_page, name="products"),
    # path('dojoswag/deletecart', views.delete_from_cart),
    # path('dojoswag/checkout', views.checkout, name="checkout"),
    # path('dojoswag/submitorder', views.submit_order),
    path('success', views.success, name="success"),
]


#####
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
