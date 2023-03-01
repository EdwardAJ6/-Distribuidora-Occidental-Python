from django.contrib import admin
# Reportes PDF (IVAN HIJUEPUTA)
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet


from .models import *

class ProductoAdmin(admin.ModelAdmin):
    fields = ('NombreProducto', 'precio', 'StockDisponible', 'Descripcion', 'FechaVencimiento', 'Foto', 'Categoria', 'Marca')
    list_display = ['__str__', 'slug']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_CategoriasProductos.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las categorias productos'
            data = [['Nombre de la categoria',]]
            for obj in queryset:

                data.append([obj.nombreCategoria])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las categorias productos", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las categorias productos'
    actions={generate_pdf}
admin.site.register(Producto,ProductoAdmin)



# @admin.register(Marca) (PAL REPORTE HIJUEPUTA)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_marca.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de los marcas'
            data = [['Nombre de la marca',]]
            for obj in queryset:

                data.append([obj.nombre])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de marcas", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de los marcas'
    actions={generate_pdf}
admin.site.register(Marca,MarcaAdmin)


# @admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreCategoria']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_CategoriasProductos.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las categorias productos'
            data = [['Nombre de la categoria',]]
            for obj in queryset:

                data.append([obj.nombreCategoria])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las categorias productos", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las categorias productos'
    actions={generate_pdf}
admin.site.register(CategoriaProducto,CategoriaProductoAdmin)


   

# @admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['primer_nombre']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_Usuario(s).pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de los usuarios'
            data = [['Numero de documento','Primer nombre','Segundo nombre','Primer apellido','Segundo apellido','Dirección','Teléfono','Email','rol','Tipo de documento',]]
            for obj in queryset:

                data.append([obj.num_doc,obj.primer_nombre,obj.segundo_nombre,obj.primer_apellido,obj.segundo_apellido,obj.direccion,obj.telefono,obj.email,obj.rol,obj.tipoDoc])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de los usuarios", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de los usuarios'
    actions={generate_pdf}
admin.site.register(Usuario,UsuarioAdmin)

# @admin.register(Peticion)
class PeticionAdmin(admin.ModelAdmin):
    list_display = ['id']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_peeticion(es).pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las peticiones'
            data = [['Descripción','Tipo de la petición','Usuario']]
            for obj in queryset:

                data.append([obj.descripcion,obj.tipoPeticion,obj.usuario])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las peticiones", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de los usuarios'
    actions={generate_pdf}
admin.site.register(Peticion,PeticionAdmin)

# @admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_respuestas.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las respuestas'
            data = [['Descripción','Petición','Usuario']]
            for obj in queryset:

                data.append([obj.descripcion,obj.peticion,obj.usuario])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las respuestas", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las peticiones'
    actions={generate_pdf}
admin.site.register(Respuesta,RespuestaAdmin)
    

# @admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_proveedores.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las respuestas'
            data = [['Nombre','Nit','Direccion','Telefono','Email']]
            for obj in queryset:

                data.append([obj.nombre,obj.nit,obj.direccion,obj.telefono,obj.email])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de los proveedores", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de los proveedores'
    actions={generate_pdf}
admin.site.register(Proveedor,ProveedorAdmin)
    

# @admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['fechaCompra']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_compras.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las compras'
            data = [['Fecha de la compra','Total','Proveedor']]
            for obj in queryset:

                data.append([obj.fechaCompra,obj.total,obj.proeveedor])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las compras", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las compras'
    actions={generate_pdf}
admin.site.register(Compra,CompraAdmin)

# @admin.register(DetalleCompra) 
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ['fecha']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_compras.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las compras'
            data = [['Id Compra','Id Producto','Fecha','precio del producto','cantidad','subotal','iva','total']]
            for obj in queryset:

                data.append([obj.idCompra,obj.idProducto,obj.fecha,obj.precioProducto,obj.cantidad,obj.subtotal,obj.iva,obj.total])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las compras", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las compras'
    actions={generate_pdf}
admin.site.register(DetalleCompra,DetalleCompraAdmin)


# @admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_inventario.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte del inventario'
            data = [['Nombre',]]
            for obj in queryset:

                data.append([obj.nombre])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte del inventario", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte del inventario'
    actions={generate_pdf}
admin.site.register(Inventario,InventarioAdmin)    
    
# @admin.register(InventarioEntrada)
class InventarioEntradaAdmin(admin.ModelAdmin):
    list_display = ['idInventario']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_inventarioE.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte del inventarioE'
            data = [['Id producto','Id inventario','cantidad','total']]
            for obj in queryset:

                data.append([obj.idProducto,obj.idInventario,obj.cantidad,obj.total])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte del inventarioE", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte del inventario'
    actions={generate_pdf}
admin.site.register(InventarioEntrada,InventarioEntradaAdmin)


# @admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['fechaVenta']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_venta.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de las ventas'
            data = [['fechaVenta','total','usuario','idProducto']]
            for obj in queryset:

                data.append([obj.fechaVenta,obj.total,obj.usuario,obj.idProducto])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de las ventas", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de las ventas'
    actions={generate_pdf}
admin.site.register(Venta,VentaAdmin)

# @admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['fecha']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_detalles_venta.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de los detalles ventas'
            data = [['fechaVenta','total','usuario','idProducto']]
            for obj in queryset:

                data.append([obj.idVenta,obj.fecha,obj.cantidad,obj.precioProducto,obj.subtotal,obj.iva,obj.total])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte de los detalles ventas", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte de los detalles ventas'
    actions={generate_pdf}
admin.site.register(DetalleVenta,DetalleVentaAdmin)

# @admin.register(InventarioSalida)
class InventarioSalidaAdmin(admin.ModelAdmin):
    list_display = ['total']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_inventarioS.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte del inventario salida'
            data = [['Id venta','Id inventario','Cantidad','Total']]
            for obj in queryset:

                data.append([obj.idVenta,obj.idInventario,obj.cantidad,obj.total])
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN',  (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            styles = getSampleStyleSheet()
            header = Paragraph("Reporte del inventario salida", style=styles['Heading1'])
            doc.build([header, tabla])

            return response
    generate_pdf.short_description = 'Reporte del inventario salida'
    actions={generate_pdf}
admin.site.register(InventarioSalida,InventarioSalidaAdmin)


class PqrAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'titulo', 'descripcion', 'creada_en']
admin.site.register(Pqr,PqrAdmin)



