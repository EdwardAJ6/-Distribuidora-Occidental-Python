# Generated by Django 4.1.7 on 2023-03-06 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orden.common


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direcciones', '0001_initial'),
        ('carrito', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_id', models.CharField(max_length=100, unique=True)),
                ('estado', models.CharField(choices=[(orden.common.OrdenEstado['CREADO'], 'CREADO'), (orden.common.OrdenEstado['PAGADO'], 'PAGADO'), (orden.common.OrdenEstado['COMPLETADA'], 'COMPLETADA'), (orden.common.OrdenEstado['CANCELADA'], 'CANCELADA')], default=orden.common.OrdenEstado['CREADO'], max_length=50)),
                ('precio_envio', models.DecimalField(decimal_places=2, default=5, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fecha_crea', models.DateTimeField(auto_now=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.carro')),
                ('direccionorden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direcciones.dirrecionesenvios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
