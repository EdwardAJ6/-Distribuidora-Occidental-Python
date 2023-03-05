from django.urls import path

from . import views

app_name = "orden"

urlpatterns = [
     path('', views.orden, name='orden'),
     path('direccion', views.address, name='direccion'),
     path('seleccionar/direccion', views.select_address, name='seleccionar'),
     path('establecer/direccion/<int:pk>', views.check_address, name='check_direccion'),
     path('confirmacion', views.confirm, name='confirmar'),
     path('cancelar', views.cancel, name='cancelar'),
     path('completar', views.complete, name='completar'),
     path('completadas', views.VistaOrdenLista.as_view(), name='completadas')
]
