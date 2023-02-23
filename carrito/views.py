from django.shortcuts import render

from .models import Carro
from .utils import crear_obtener_carrito

def carro(request):

    carrito = crear_obtener_carrito(request)

    return render(request, 'carro.html', { 
})
