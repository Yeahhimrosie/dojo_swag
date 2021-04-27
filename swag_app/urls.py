from django.contrib import admin
from django.urls import path
from . import views
####
# from django.conf import settings
# from django.conf.urls.static import static

#Roy will handle urls

urlpatterns = [
    path('', views.swag_home),
    path('dojoswag/productpage/<int:product_id>', views.product_page),
    # path('dojoswag/checkoutpage', views.checkout_page),
    # path('dojoswag/cartpage', views.cart_page),
    # path('dojoswag/addcart', views.add_to_cart),
    # path('dojoswag/deletecart', views.delete_from_cart),
    # path('dojoswag/checkout', views.checkout),
    # path('dojoswag/submitorder', views.submit_order),
]

#####
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)