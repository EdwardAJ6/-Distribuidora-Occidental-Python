from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from direcciones.models import DirrecionesEnvios
from .utils import crear_obtener_orden
from carrito.utils import crear_obtener_carrito
from .models import Orden

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def orden(request):
    carrito = crear_obtener_carrito(request)
    orden = crear_obtener_orden(carrito, request)
    
    return render(request, 'ordenes/ordenar.html', {
        'carrito':carrito,
        'orden':orden,
    })

@login_required(login_url='login')
def address(request):
   carrito = crear_obtener_carrito(request)
   orden = crear_obtener_orden(carrito,request)

   direcciones = orden.get_or_set_shipping_address()
   
   return render(request, 'ordenes/direcciones.html', {
      'carrito':carrito,
      'orden':orden,
      'direcciones': direcciones
    })

@login_required(login_url='login')
def select_address(request):
    direcciones = request.user.dirrecionesenvios_set.filter(default=False)

    return render(request, 'ordenes/select_direccion.html', {
        'direcciones': direcciones,
    })

@login_required(login_url='login')
def check_address(request, pk):
    carrito = crear_obtener_carrito(request)
    orden = crear_obtener_orden(carrito,request)
    
    direcciones = get_object_or_404(DirrecionesEnvios, pk=pk)

    if request.user.id != direcciones.user_id:
        return redirect('carrito:carro')
    
    orden.update_shipping_direccion(direcciones)

    return redirect('orden:direccion')