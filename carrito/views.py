from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Carro
from .utils import crear_obtener_carrito
from core.models import Producto

def carro(request):

    carrito = crear_obtener_carrito(request)
    
    return render(request, 'carro.html', { 
     'carrito':carrito                                     
})

def agregar(request):
    carrito = crear_obtener_carrito(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))

    carrito.productos.add(producto) 

    return render(request, 'carrito/agregado.html', {
        'producto' : producto
    })

def eliminar(request):
    carrito = crear_obtener_carrito(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
    
    carrito.productos.remove(producto)
    
    return redirect('carrito:carro')
     