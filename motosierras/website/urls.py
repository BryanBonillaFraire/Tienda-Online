from django.urls import path
from .views import index, store, cart, checkout

urlpatterns = [
    path('', index, name="index"),
    path('store/', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
]
