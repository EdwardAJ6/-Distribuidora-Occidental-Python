# Generated by Django 4.1.7 on 2023-02-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_compra_inventario_proveedor_alter_respuesta_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
