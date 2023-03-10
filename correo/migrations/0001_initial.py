# Generated by Django 4.1.7 on 2023-03-06 01:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('destinatario', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CorreoMasivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('enviado', models.BooleanField(default=False)),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('destinatarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
