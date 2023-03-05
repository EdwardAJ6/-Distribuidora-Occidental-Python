from django.shortcuts import render,redirect
from .models import Producto
from .models import  Transaccion
from core.models import Proveedor
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Sum
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def registrar_transaccion(request, proveedor_id=None):
    proveedores = Proveedor.objects.all()
    if proveedor_id:
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        productos = Producto.objects.filter(proveedor=proveedor).select_related('proveedor')
    else:
        proveedor = None
        productos = Producto.objects.select_related('proveedor').all()

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        producto_id = request.POST.get('producto')    

        if 'cantidad' in request.POST:
         cantidad = int(request.POST['cantidad'])
        else:
         cantidad = 0  # o cualquier otro valor predeterminado
        try:
         producto = Producto.objects.get(pk=producto_id)

        except Producto.DoesNotExist:
            messages.error(request, f"El producto con ID {producto_id} no existe.")
            return redirect('registrar_transaccion', proveedor_id=proveedor_id)
        if tipo == 'entrada':
            producto.cantidad += cantidad
        elif tipo == 'salida':
            if cantidad > producto.cantidad:
                # No se puede registrar una salida mayor que la cantidad actual
                messages.error(request, "La cantidad de salida es mayor que la cantidad actual del producto.")
                return redirect('inventario/registrar_transaccion', proveedor_id=proveedor_id)
            
            producto.cantidad -= cantidad
        transaccion = Transaccion(tipo=tipo, producto=producto, cantidad=cantidad, usuario=request.user)
        transaccion.save()
        producto.save()

        messages.success(request, "Transacción registrada exitosamente.")
        return redirect('registrar_transaccion')
    return render(request, 'inventario/registrar_transaccion.html', {'productos': productos, 'proveedores': proveedores, 'proveedor': proveedor})

def mostrar_productos(request):
    productos_pocos = Producto.objects.filter(cantidad__lt=10)
    for producto in productos_pocos:
        messages.warning(request, f"El producto {producto.NombreProducto} tiene menos de 10 unidades")

    context = {'productos': productos_pocos }
    return render(request, 'inventario/productos.html', context)

def reporte_movimientos_inventario(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        transacciones = Transaccion.objects.filter(fechaDos__range=[fecha_inicio, fecha_fin])

        entradas = transacciones.filter(tipo='entrada').values('producto__NombreProducto').annotate(total=Sum('cantidad'))
        salidas = transacciones.filter(tipo='salida').values('producto__NombreProducto').annotate(total=Sum('cantidad'))

        datos = {}

        for entrada in entradas:
            nombre = entrada['producto__NombreProducto']
            if nombre not in datos:
                datos[nombre] = {'entradas': 0, 'salidas': 0}
            datos[nombre]['entradas'] = entrada['total']

        for salida in salidas:
            nombre = salida['producto__NombreProducto']
            if nombre not in datos:
                datos[nombre] = {'entradas': 0, 'salidas': 0}
            datos[nombre]['salidas'] = salida['total']

        nombres = []
        entradas = []
        salidas = []

        for nombre, datos_producto in datos.items():
            nombres.append(nombre)
            entradas.append(datos_producto['entradas'])
            salidas.append(datos_producto['salidas'])

        return render(request, 'inventario/reporteSaliEn.html', {
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'nombres': nombres,
            'entradas': entradas,
            'salidas': salidas
        })

    return render(request, 'inventario/filtro_fechas_reporte_movimientos_inventario.html')

