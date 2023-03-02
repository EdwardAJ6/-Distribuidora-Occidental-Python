from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Producto

class VistaListaProductos(ListView):
    template_name = 'tienda/tienda.html'
    queryset = Producto.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['message'] = 'Lista De Productos' 
          
        return context

class VistaDetalleProducto(DetailView):
    model = Producto
    template_name = 'tienda/producto.html'
    
    
class VistaListaBuscarProductos(ListView):
    template_name = 'productos/buscar.html'
    
    def get_queryset(self):
        return Producto.objects.filter(NombreProducto__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['query'] = self.query()
          
        return context