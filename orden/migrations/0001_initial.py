# Generated by Django 4.1.7 on 2023-03-05 18:15

from django.db import migrations, models
import django.db.models.deletion
import orden.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrito', '0001_initial'),
        ('direcciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_id', models.CharField(max_length=100, unique=True)),
                ('estado', models.CharField(choices=[(orden.models.OrdenEstado['CREADO'], 'CREADO'), (orden.models.OrdenEstado['PAGADO'], 'PAGADO'), (orden.models.OrdenEstado['COMPLETADA'], 'COMPLETADO'), (orden.models.OrdenEstado['CANCELADA'], 'CANCELADO')], default=orden.models.OrdenEstado['CREADO'], max_length=50)),
                ('precio_envio', models.DecimalField(decimal_places=2, default=5, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fecha_crea', models.DateTimeField(auto_now=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.carro')),
                ('direccionorden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direcciones.dirrecionesenvios')),
            ],
        ),
    ]
