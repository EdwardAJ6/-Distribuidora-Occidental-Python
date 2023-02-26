from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carro, name='carro'),
    path('agregar', views.agregar, name='agregar'),
    path('eliminar', views.eliminar, name='eliminar')
]