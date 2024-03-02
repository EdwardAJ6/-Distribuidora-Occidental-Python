#!/bin/bash

#Creando migraciones
echo "Migraciones"
python manage.py makemigrations

# Aplica las migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Inicia el servidor
echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8000
