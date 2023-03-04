# Generated by Django 4.1.7 on 2023-03-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_pqr_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqr',
            name='fecha_respuesta',
            field=models.DateField(null=True, verbose_name='Respondida en'),
        ),
        migrations.AddField(
            model_name='pqr',
            name='respuesta',
            field=models.TextField(max_length=500, null=True, verbose_name='Respuesta'),
        ),
    ]
