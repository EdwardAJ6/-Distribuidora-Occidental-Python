from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid


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

class Producto(models.Model):
    NombreProducto = models.CharField(max_length=100,verbose_name='Nombre')
    precio = models.PositiveBigIntegerField(verbose_name='Precio')
    StockDisponible = models.PositiveIntegerField(verbose_name='Stoc kDisponible')
    Descripcion = models.CharField(max_length=255,verbose_name='Descripcion')
    FechaVencimiento = models.DateField()
    Foto = models.ImageField()
    Categoria = models.ManyToManyField(CategoriaProducto, verbose_name='Categoría')
    Marca = models.ForeignKey(Marca,on_delete=models.CASCADE, verbose_name='Marca')
    slug = models.SlugField(null=False, blank=False, unique=True)
    
#   def save(self, *args, **kwargs):
#       self.slug = slugify(self.NombreProducto)
#       super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return (self.NombreProducto)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
    
def set_slug(sender, instance, *args, **kwargs):
    slug = instance.slug or slugify(instance.NombreProducto)  # Asigna un valor predeterminado si instance.slug no está definido

    while Producto.objects.filter(slug=slug).exists():
        slug = slugify(
            '{}-{}'.format(instance.NombreProducto, str(uuid.uuid4())[:8])
        )
    instance.slug = slug


pre_save.connect(set_slug, sender=Producto)

class Rol(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'rol'

ROL_CHOICES =(
    ("1", "Administrador"),
    ("2", "Usuario"),
)
TIPODOC_CHOICES =(
    ("C.C", "'Cédula de ciudadanía"),
    ("T.I", "Tarjeta de identidad"),
)

class Usuario(models.Model):
    num_doc = models.CharField(max_length=20, unique=True,verbose_name="Numero de documento")
    primer_nombre = models.CharField(max_length=50,verbose_name="Primer Nombre")
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True,verbose_name="Segundo nombre")
    primer_apellido = models.CharField(max_length=50,verbose_name="Primer Apellido")
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True,verbose_name="Segundo Apellido")
    direccion = models.CharField(max_length=200, blank=True, null=True,verbose_name="Direccion")
    telefono = models.CharField(max_length=20, blank=True, null=True,verbose_name="Telefono")
    email = models.EmailField(max_length=254, unique=True,verbose_name="Email")
    contraseña = models.CharField(max_length=20,verbose_name="Contraseña")
    rol = models.CharField(max_length=50,choices=ROL_CHOICES, verbose_name="Rol")
    tipoDoc = models.CharField(max_length=50,choices=TIPODOC_CHOICES,verbose_name="Tipo de documento")

    def __str__(self):
        return self.primer_nombre

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

TIPOPETI_CHOICES =(
    ("Queja", "Queja"),
    ("Reclamo", "Reclamo "),
    ("Peticion", "Peticion"),

)

class Peticion(models.Model):
    descripcion = models.CharField(max_length=255,verbose_name='Descripcion')
    tipoPeticion = models.CharField(max_length=50,choices=TIPOPETI_CHOICES)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, verbose_name='Usuario',null=True, blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Peticion'
        verbose_name_plural = 'Peticiones'
        db_table = 'peticion'

class Respuesta(models.Model):
    descripcion = models.CharField(max_length=255,verbose_name='Descripcion')
    peticion = models.ForeignKey(Peticion,on_delete=models.CASCADE, verbose_name='Peticion')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuario')

    
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        db_table = 'respuesta'

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


class Compra(models.Model):
    fechaCompra = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField(verbose_name='Total')
    proeveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,verbose_name='Proveedor')
  
    def __str__(self):
        return self.fechaCompra

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compra'

class DetalleCompra(models.Model):
    idCompra = models.ForeignKey(Compra,on_delete=models.CASCADE, verbose_name='Compra')
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name='Producto')
    fecha = models.DateField(auto_now_add=True)
    precioProducto = models.PositiveIntegerField(verbose_name='Precio del producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    subtotal = models.PositiveIntegerField(verbose_name='Subtotal')
    iva = models.PositiveIntegerField(verbose_name='iva')
    total = models.PositiveIntegerField(verbose_name='Total')
      
    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name = 'DetalleCompra'
        verbose_name_plural = 'DetallesCompras'
        db_table = 'detalleCompra'

class Inventario(models.Model):
    nombre = models.CharField(max_length=50,verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventario'

class InventarioEntrada(models.Model):
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name='Producto')
    idInventario = models.ForeignKey(Inventario,on_delete=models.CASCADE, verbose_name='Inventario')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    total = models.PositiveIntegerField(verbose_name='Total')

    def __str__(self):
        return self.cantidad

    class Meta:
        verbose_name = 'InventarioEntrada'
        verbose_name_plural = 'InventariosEntradas'
        db_table = 'inventarioEntrada'


class Venta(models.Model):
    fechaVenta = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField(verbose_name='Total')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuario')
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return self.fechaVenta

    class Meta:
        verbose_name = 'Ventas'
        verbose_name_plural = 'Ventas'
        db_table = 'ventas'

class DetalleVenta(models.Model):

    idVenta = models.ForeignKey(Venta,on_delete=models.CASCADE, verbose_name='Venta')
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precioProducto = models.PositiveIntegerField(verbose_name='Precio del producto')
    subtotal = models.PositiveIntegerField(verbose_name='Subtotal')
    iva = models.PositiveIntegerField(verbose_name='iva')
    total = models.PositiveIntegerField(verbose_name='Total')
      

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name = 'DetalleVenta'
        verbose_name_plural = 'DetallesVentas'
        db_table = 'detalleVentas'

class InventarioSalida(models.Model):
    idVenta = models.ForeignKey(Venta,on_delete=models.CASCADE, verbose_name='Venta')
    idInventario = models.ForeignKey(Inventario,on_delete=models.CASCADE, verbose_name='Inventario')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    total = models.PositiveIntegerField(verbose_name='Total')

    def __str__(self):
        return self.cantidad

    class Meta:
        verbose_name = 'InventarioSalida'
        verbose_name_plural = 'InventariosSalidas'
        db_table = 'inventarioSalida'

@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='User')
        instance.groups.add(group)










