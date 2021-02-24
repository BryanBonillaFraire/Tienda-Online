from django.shortcuts import render
#from django.views.generic import CreateView
from .models import *

def index(request):
    return render(request, 'index.html', {})
def store(request):
    productos = Producto.objects.all()
    context = {'producto':productos}
    return render(request, 'store.html', context)
def cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        envio, created = Envio.objects.get_or_create(cliente=cliente, complete=False)
        items = envio.objetosenvio_set.all()
    else:
        items=[]
        envio={'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items,
        'envio':envio,}

    return render(request, 'cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        envio, created = Envio.objects.get_or_create(cliente=cliente, complete=False)
        items = envio.objetosenvio_set.all()
    else:
        items=[]
        envio={'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items,
        'envio':envio,}

    return render(request, 'checkout.html', context)
