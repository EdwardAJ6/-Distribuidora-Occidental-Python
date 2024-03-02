# Usa la imagen oficial de Python como base
FROM python:3.9
# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt /app/

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio /app en el contenedor
COPY . /app/

# Expone el puerto 8000 para que la aplicación Django pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Copia el script .sh al directorio raíz del contenedor
COPY start.sh /start.sh

# Otorga permisos de ejecución al script .sh
RUN chmod +x /start.sh

# Ejecuta el script .sh para realizar las migraciones de Django, aplicarlas y luego iniciar el servidor
CMD ["/bin/bash", "/start.sh"]