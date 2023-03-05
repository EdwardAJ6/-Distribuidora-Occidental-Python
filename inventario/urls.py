from django.urls import path
from .views import  registrar_transaccion,mostrar_productos,reporte_movimientos_inventario

urlpatterns = [

    path('transaccion/', registrar_transaccion, name='registrar_transaccion'),
    path('transaccion//', registrar_transaccion, name='registrar_transaccion'),

    path('transaccion/<int:proveedor_id>/', registrar_transaccion, name='registrar_transaccion_proveedor'),
    path('productos/', mostrar_productos, name='productosbajos'),
    path('reporte/', reporte_movimientos_inventario, name='reporte_movimientos_inventario'),



]