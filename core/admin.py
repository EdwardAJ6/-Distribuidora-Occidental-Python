import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from django.contrib import admin
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

                data.append([obj.Categoria])
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
    def reporte_stock_pdf(modeladmin, request, queryset):
        stock = queryset.values_list('NombreProducto', 'StockDisponible')

        # Crear una figura de Matplotlib con el gráfico de barras del stock
        fig, ax = plt.subplots()
        ax.bar(*zip(*stock))
        ax.set_xlabel('Productos')
        ax.set_ylabel('Stock')
        ax.set_title('Stock de productos')

        # Guardar la figura en un archivo PDF utilizando BytesIO
        buffer = BytesIO()
        plt.savefig(buffer, format='pdf')
        buffer.seek(0)

        # Devolver un objeto HttpResponse con el contenido del archivo PDF
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=reporte_stock.pdf'
        return response
    reporte_stock_pdf.short_description = 'Generar reporte de stock en PDF'


    generate_pdf.short_description = 'Reporte de las categorias productos'
    actions = [reporte_stock_pdf, generate_pdf]
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
    def reporte_marcas_pdf(modeladmin, request, queryset):
        # Obtener la cantidad de marcas
        cantidad_marcas = queryset.count()

        # Crear una figura de Matplotlib con el gráfico de barras de la cantidad de marcas
        fig, ax = plt.subplots()
        ax.bar(['Marcas'], [cantidad_marcas])
        ax.set_xlabel('Marcas')
        ax.set_ylabel('Cantidad')
        ax.set_title('Cantidad de marcas')

        # Guardar la figura en un archivo PDF utilizando BytesIO
        buffer = BytesIO()
        plt.savefig(buffer, format='pdf')
        buffer.seek(0)

        # Devolver un objeto HttpResponse con el contenido del archivo PDF
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=reporte_marcas.pdf'
        return response
    reporte_marcas_pdf.short_description = 'Generar reporte de marcas en PDF'

    generate_pdf.short_description = 'Reporte de los marcas'
    actions = [reporte_marcas_pdf,generate_pdf]
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



