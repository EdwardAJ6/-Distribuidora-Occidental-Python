import uuid
import decimal 

from django.db import models
from usuario.models import User
from core.models import Producto
from orden.common import OrdenEstado

from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed

class Carro(models.Model):
    carrito_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 
    productos = models.ManyToManyField(Producto, through='ProductosCarro')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    
    FEE = 0.19

    def __str__(self):
        return self.carrito_id
    
    def update_totals(self):
        self.update_subtotals()
        self.update_total()
        
        if self.orden:
            self.orden.update_total()
        
    def update_subtotals(self):
        self.subtotal = sum([
           cp.cantidad * cp.producto.precio for cp in self.products_related()
        ])
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Carro.FEE))
        self.save()

    def products_related(self):
        return self.productoscarro_set.select_related('producto')

    @property
    def orden(self):
       return self.orden_set.filter(estado=OrdenEstado.CREADO).first()

        
class ProductosCarroManager(models.Manager):
    
    def crear_o_actualiza_cantidad(self, carrito, producto, cantidad=1):
        objects, created = self.get_or_create(carrito=carrito, producto=producto)
        
        if not created:
            cantidad = objects.cantidad + cantidad
        
        objects.actualizar_cantidad(cantidad)
        return objects
        
class ProductosCarro(models.Model):
    carrito = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    
    objects = ProductosCarroManager()
    
    def actualizar_cantidad(self, cantidad=1):
        self.cantidad = cantidad
        self.save()

def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs ):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.carrito.update_totals()

pre_save.connect(set_carrito_id, sender=Carro)
post_save.connect(post_save_update_totals, sender=ProductosCarro)
m2m_changed.connect(update_totals, sender=Carro.productos.through)