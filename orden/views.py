from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from direcciones.models import DirrecionesEnvios
from .utils import crear_obtener_orden
from .utils import destruir_orden
from carrito.utils import crear_obtener_carrito
from carrito.utils import destruir_carrito
from .models import Orden
from django.contrib import messages
from .mails import Mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
from django.contrib.auth.decorators import login_required
import threading
from django.db import transaction
from inventario.models import Transaccion


class VistaOrdenLista(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'ordenes/ordenes.html'
    
    def get_queryset(self):
        return self.request.user.ordenes_completadas()

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

@login_required(login_url='login')
def confirm(request):
    carrito = crear_obtener_carrito(request)
    orden = crear_obtener_orden(carrito, request)
    
    direccionorden = orden.direccionorden
    if direccionorden is None:
        return redirect('orden:direccion')
    
    return render(request, 'ordenes/confirmar.html', {
        'carrito' : carrito,
        'orden' : orden, 
        'direccionorden' : direccionorden
    })

@login_required(login_url='login')    
def cancel(request):
    carrito = crear_obtener_carrito(request)
    orden = crear_obtener_orden(carrito, request)
    
    if request.user.id != orden.usuario_id:
        return redirect('carrito:carrito')
    
    orden.cancel()
    
    destruir_carrito(request)
    destruir_orden(request)
    
    messages.error(request, 'Orden Cancelada')
    return redirect('tienda')

@login_required(login_url='login')   
def complete(request):
    carrito = crear_obtener_carrito(request)
    orden = crear_obtener_orden(carrito, request)
    
    if request.user.id != orden.usuario_id:
        return redirect('carrito:carrito')
    
    orden.complete()
    # Restar la cantidad de productos en el carrito
    for producto_carrito in carrito.productoscarro_set.all():
        producto = producto_carrito.producto
        cantidad_carrito = producto_carrito.cantidad
        cantidad = producto.cantidad
        
        producto.cantidad = cantidad - cantidad_carrito
        producto.save()

        # Crear un registro en la tabla de Transaccion por cada producto
        with transaction.atomic():
            transaccion = Transaccion.objects.create(
                tipo='salida',
                producto=producto,
                cantidad=cantidad_carrito,
                usuario=request.user,
            )
    
    thread = threading.Thread(target=Mail.enviar_orden_completada, args=(
        orden, request.user
    ))
    thread.start()
    
    destruir_carrito(request)
    destruir_orden(request)
    
    messages.success(request, 'Compra completada exitosamente')
    return redirect('tienda')