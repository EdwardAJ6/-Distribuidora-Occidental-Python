import uuid
from django.db import models
from usuario.models import User
from carrito.models import Carro
from .common import OrdenEstado
from .common import choices
from enum import Enum
from direcciones.models import DirrecionesEnvios

from django.db.models.signals import pre_save
class Orden(models.Model):
    orden_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=choices, default=OrdenEstado.CREADO)
    
    precio_envio = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    fecha_crea = models.DateTimeField(auto_now=True)
    direccionorden = models.ForeignKey(DirrecionesEnvios, #Una dirección de envío puede tener muchas ordenes
                                            null=True, blank=True,
                                            on_delete=models.CASCADE)
    def __str__(self):
        return self.orden_id
    
    def cancel(self):
        self.status = OrdenEstado.CANCELADA
        self.save()
    
    def complete(self):
        self.estado = OrdenEstado.COMPLETADA
        self.save()
        
    def update_total(self):
        self.total = self.get_total()
        self.save()
    
    def get_total(self):
        return self.carrito.total + self.precio_envio
    
    def update_shipping_direccion(self,direccionorden):
        self.direccionorden = direccionorden
        self.save()
    
    def get_or_set_shipping_address(self):
        if self.direccionorden:
            return self.direccionorden

        direccionorden = self.usuario.shipping_address

        if direccionorden:
            self.direccionorden = direccionorden
            self.save()

        return direccionorden
    
    
def set_orden_id(sender, instance, *args, **kwargs):
    if not instance.orden_id:
        instance.orden_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()

pre_save.connect(set_orden_id, sender=Orden)
pre_save.connect(set_total, sender=Orden)