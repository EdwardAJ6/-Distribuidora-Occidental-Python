from django.db import models

from django.contrib.auth.models import AbstractUser
from orden.common import OrdenEstado

TIPODOC_CHOICES =(
    ("C.C", "'Cédula de ciudadanía"),
    ("T.I", "Tarjeta de identidad"),
)


#Esta es la tabla que se está usando para las PQRS 
class User(AbstractUser):
   
   telefono = models.CharField(max_length=20, blank=True, null=True,verbose_name="Telefono")
   tipoDoc = models.CharField(max_length=50,choices=TIPODOC_CHOICES,blank=True, null=True,verbose_name="Tipo de documento")
   primer_apellido = models.CharField(max_length=50,blank=True, null=True,verbose_name="Primer Apellido")
   segundo_apellido = models.CharField(max_length=50, blank=True, null=True,verbose_name="Segundo Apellido")     


   def get_full_name(self):
     return '{} {}'.format(self.first_name, self.segundo_apellido) 

   @property
   def shipping_address(self):
        return self.dirrecionesenvios_set.filter(default=True).first()

   def has_direcciones(self):
        return self.shipping_address is not None
    
   def ordenes_completadas(self):
        return self.orden_set.filter(estado=OrdenEstado.COMPLETADA).order_by('-id')

class Customer(User):
    class Meta:
        proxy = True 

    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
