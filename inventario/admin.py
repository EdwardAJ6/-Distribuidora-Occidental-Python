from django.contrib import admin
from .models import Transaccion,Inventario,Compra
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from django.db.models import Count
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors





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

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['producto','fecha']
    list_filter = ['fecha']

    fields = ('producto','cantidad','total')
    def generate_pdf(self, request, queryset):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="reporte_Compras.pdf"'
            doc = SimpleDocTemplate(response, pagesize=landscape(letter))
            doc.title = 'Reporte de Compras'
            data = [['Nombre del produto','Cantidad','Fecha','Total']]
            for obj in queryset:

                data.append([obj.producto,obj.cantidad,obj.fecha,obj.total])
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
    actions = [ generate_pdf]

