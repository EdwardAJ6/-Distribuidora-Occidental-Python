from django.contrib import admin
from .models import Transaccion,Inventario


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'producto', 'cantidad', 'precio_producto', 'total']
    list_filter = ['tipo']

    def precio_producto(self, obj):
        return obj.producto.precio

    def total(self, obj):
        return obj.cantidad * obj.producto.precio

    precio_producto.short_description = 'Precio'
    total.short_description = 'Total'

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
     list_display = ['ubicacion','producto']
