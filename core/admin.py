from django.contrib import admin
# Reportes PDF (IVAN HIJUEPUTA)
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet


from .models import *

class ProductoAdmin(admin.ModelAdmin):
    fields = ('NombreProducto', 'precio', 'cantidad', 'Descripcion', 'FechaVencimiento', 'Foto', 'Categoria', 'Marca','proveedor')
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

class PqrAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'titulo', 'descripcion', 'creada_en']
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_pqrs.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de PQRS'
            data = [['Creado por','Titulo','Descripción','Creada en']]
            for obj in queryset:

                data.append([obj.usuario,obj.titulo,obj.descripcion,obj.creada_en])
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
            header = Paragraph("Reporte de PQRS", style=styles['Heading1'])
            doc.build([header, tabla])
            return response

    generate_pdf.short_description = 'Reporte de PQRS'
    actions={generate_pdf}

admin.site.register(Pqr,PqrAdmin)
