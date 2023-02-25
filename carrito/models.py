import uuid
from django.db import models
from usuario.models import User
from core.models import Producto

from django.db.models.signals import pre_save

class Carro(models.Model):
    carrito_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    productos = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    fecha_crea = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id

def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())

pre_save.connect(set_carrito_id, sender=Carro)