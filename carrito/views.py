from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import ProductosCarro
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
    cantidad = int(request.POST.get('cantidad', 1))
    
#    carrito.productos.add(producto, through_defaults={
#        'cantidad':cantidad
#    }) 

    producto_carro = ProductosCarro.objects.crear_o_actualiza_cantidad(
        carrito=carrito, producto=producto, cantidad=cantidad)

    return render(request, 'carrito/agregado.html', {
        'cantidad': cantidad,
        'producto' : producto
    })

def eliminar(request):
    carrito = crear_obtener_carrito(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
    
    carrito.productos.remove(producto)
    
    return redirect('carrito:carro')
     