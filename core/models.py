from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid
from usuario.models import User
from django.contrib.auth.models import Group

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marca'

class CategoriaProducto(models.Model):
    nombreCategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreCategoria

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categorias_productos'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    nit = models.PositiveIntegerField(verbose_name='NIT')
    direccion = models.CharField(max_length=200, blank=True, null=True,verbose_name="Direccion")
    telefono = models.CharField(max_length=20, blank=True, null=True,verbose_name="Telefono")
    email = models.EmailField(max_length=254, unique=True,verbose_name="Email")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'

class Producto(models.Model):
    NombreProducto = models.CharField(max_length=100,verbose_name='Nombre')
    precio = models.PositiveBigIntegerField(verbose_name='Precio')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    Descripcion = models.CharField(max_length=255,verbose_name='Descripcion')
    FechaVencimiento = models.DateField()
    Foto = models.ImageField()
    Categoria = models.ManyToManyField(CategoriaProducto, verbose_name='Categoría')
    Marca = models.ForeignKey(Marca,on_delete=models.CASCADE, verbose_name='Marca')
    slug = models.SlugField(null=True, blank=True, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    
    def __str__(self):
        return (self.NombreProducto)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
    
def set_slug(sender, instance, *args, **kwargs):
    if instance.NombreProducto:
        slug = slugify(instance.NombreProducto)

        while Producto.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.NombreProducto, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Producto)

@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='User')
        instance.groups.add(group)


class Pqr(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Creada por')
    titulo = models.CharField(max_length=30,verbose_name='Título')
    ELECCIONES = [   ('Peticion', 'Peticion'),   ('Queja', 'Queja'),   ('Reclamo', 'Reclamo'),   ('Sugerencia', 'Sugerencia')]
    tipo = models.CharField(max_length=10, choices=ELECCIONES)
    descripcion = models.TextField(verbose_name='Descripción')
    creada_en = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    respuesta = models.TextField(max_length=500,verbose_name= 'Respuesta',null=True)
    fecha_respuesta = models.DateField(verbose_name='Respondida en',null=True)










