from django.urls import path
from . import views

urlpatterns = [
    path('buscar', views.VistaListaBuscarProductos.as_view(), name='busca'),
    path('<slug:slug>', views.VistaDetalleProducto.as_view(), name='producto'),

]