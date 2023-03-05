from .models import Orden

def crear_obtener_orden(carrito, request):
    orden = carrito.orden
    
    if orden is None and request.user.is_authenticated:
        orden = Orden.objects.create(carrito=carrito, usuario=request.user)
    
    if orden:
        request.session['orden_id'] = orden.orden_id
    
    return orden

def destruir_orden(request):
    request.session['orden_id'] = None