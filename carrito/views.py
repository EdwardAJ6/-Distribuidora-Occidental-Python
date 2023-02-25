from django.shortcuts import render

from .models import Carro
from .utils import crear_obtener_carrito
from core.models import Producto

def carro(request):

    carrito = crear_obtener_carrito(request)

    return render(request, 'carro.html', { 
})

def agregar(request):
    carrito = crear_obtener_carrito(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))

    carrito.productos.add(producto) 

    return render(request, 'carrito/agregado.html', {
        'producto' : producto
    })