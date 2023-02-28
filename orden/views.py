from django.shortcuts import render

from .utils import crear_obtener_orden
from carrito.utils import crear_obtener_carrito
from .models import Orden

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def orden(request):
    carrito = crear_obtener_carrito( request)
    orden = crear_obtener_orden(carrito, request)
    
    return render(request, 'ordenes/orden.html', {
        'carrito':carrito,
        'orden':orden,
    })
