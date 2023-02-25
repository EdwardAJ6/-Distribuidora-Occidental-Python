from django.contrib import admin

from .models import *

class ProductoAdmin(admin.ModelAdmin):
    fields = ('NombreProducto', 'precio', 'StockDisponible', 'Descripcion', 'FechaVencimiento', 'Foto', 'Categoria', 'Marca')
    list_display = ['__str__', 'slug']

admin.site.register(Producto, ProductoAdmin)
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreCategoria']

#@admin.register(Producto)
#class ProductoAdmin(admin.ModelAdmin):
#   list_display = ['NombreProducto']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['primer_nombre']

@admin.register(Peticion)
class PeticionAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['descripcion']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['fechaCompra']

@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ['fecha']

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(InventarioEntrada)
class InventarioEntradaAdmin(admin.ModelAdmin):
    list_display = ['idInventario']

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['fechaVenta']

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['fecha']

@admin.register(InventarioSalida)
class InventarioSalidaAdmin(admin.ModelAdmin):
    list_display = ['total']

    