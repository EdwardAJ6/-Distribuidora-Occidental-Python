from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.VistaDetalleProducto.as_view(), name='producto'),

]