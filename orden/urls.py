from django.urls import path

from . import views

app_name = "orden"

urlpatterns = [
     path('', views.orden, name='orden'),
     path('direccion', views.address, name='direccion'),
     path('seleccionar/direccion', views.select_address, name='seleccionar'),
     path('establecer/direccion/<int:pk>', views.check_address, name='check_direccion')


]
