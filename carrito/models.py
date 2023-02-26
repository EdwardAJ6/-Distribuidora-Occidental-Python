import uuid
import decimal 

from django.db import models
from usuario.models import User
from core.models import Producto

from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

class Carro(models.Model):
    carrito_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    productos = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    
    FEE = 0.19

    def __str__(self):
        return self.carrito_id
    
    def update_totals(self):
        self.update_subtotals()
        self.update_total()
        
    def update_subtotals(self):
        self.subtotal = sum([producto.precio for producto in self.productos.all()])
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Carro.FEE))
        self.save()


def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs ):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_carrito_id, sender=Carro)
m2m_changed.connect(update_totals, sender=Carro.productos.through)