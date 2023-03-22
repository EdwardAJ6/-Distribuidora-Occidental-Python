from django.db import models
from usuario.models import User
from django.db.models.signals import post_save
from core.models import Producto
from django.dispatch import receiver


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.ubicacion 

class Transaccion(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida')
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaDos = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.producto.NombreProducto

@receiver(post_save, sender=Producto)
def actualizar_cantidad_inventario(sender, instance, **kwargs):
    try:
        # Buscar el registro correspondiente en el modelo Inventario
        inventario = Inventario.objects.get(producto=instance)
    except Inventario.DoesNotExist:
        # Si no existe, crear un nuevo registro en el modelo Inventario
        inventario = Inventario(producto=instance, cantidad=0)
    
    # Actualizar la cantidad del inventario
    inventario.cantidad = instance.cantidad

    # Guardar los cambios en el modelo Inventario
    inventario.save()


@receiver(post_save, sender=Inventario)
def actualizar_ubicacion(sender, instance, created, **kwargs):
    if created:
        instance.ubicacion = "Bodega"
        instance.save()

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
