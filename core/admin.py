import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
#Reportes gráficos 
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from django.db.models import Count
from reportlab.lib.utils import ImageReader


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
        stock = queryset.values_list('NombreProducto', 'cantidad')

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
    list_display = ['usuario', 'titulo', 'descripcion', 'tipo', 'creada_en', 'respuesta', 'fecha_respuesta']
    readonly_fields = ('usuario', 'titulo', 'tipo', 'descripcion','creada_en')
    list_filter = ['creada_en', 'tipo', 'fecha_respuesta', 'respuesta']
    def has_add_permission(self, request):
        return False
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_pqrs.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de PQRS'
            data = [['Creado por','Titulo','Descripción','Creada en', 'respuesta', 'fecha_respuesta']]
            for obj in queryset:

                data.append([obj.usuario,obj.titulo,obj.descripcion,obj.creada_en,obj.respuesta,obj.fecha_respuesta])
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
    
    def reporte_pqrs(self, request, queryset):
    # Obtener los tipos de PQRS y sus cantidades
        tipos_pqrs = queryset.values_list('tipo').annotate(total=Count('tipo'))
    
        # Crear una lista con los tipos de PQRS y sus cantidades
        labels = [tipo[0] for tipo in tipos_pqrs]
        values = [tipo[1] for tipo in tipos_pqrs]
        
        # Crear el gráfico de pastel
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Asegurar que el gráfico sea un círculo
        
        # Guardar el gráfico en un archivo temporal
        tmpfile = BytesIO()
        plt.savefig(tmpfile, format='png')
        plt.close(fig1)
        
        # Crear el PDF y agregar el gráfico
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_pqrs.pdf"'
        
        pdf = canvas.Canvas(response)
        pdf.drawString(100, 400, "Reporte de PQRS")
        pdf.drawImage(ImageReader(tmpfile), 0, 400)
        pdf.showPage()
        pdf.save()
        
        # Devolver la respuesta con el PDF generado
        return response

    reporte_pqrs.short_description = "Generar reporte de PQRS"
    
  
    

    
    generate_pdf.short_description = 'Reporte de PQRS'
    actions={generate_pdf,reporte_pqrs}
        
admin.site.register(Pqr,PqrAdmin)






