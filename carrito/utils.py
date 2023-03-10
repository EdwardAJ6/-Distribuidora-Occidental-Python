from .models import Carro

def crear_obtener_carrito(request):
    usuario = request.user if request.user.is_authenticated else None
    carrito_id = request.session.get('carrito_id')
    carrito = Carro.objects.filter(carrito_id=carrito_id).first()

    if carrito is None:
        carrito  = Carro.objects.create(usuario=usuario)
    
    if usuario and carrito.usuario is None:
        carrito.usuario = usuario
        carrito.save()

    request.session['carrito_id'] = carrito.carrito_id

    return carrito

def destruir_carrito(request):
    request.session['carrito_id'] = None
