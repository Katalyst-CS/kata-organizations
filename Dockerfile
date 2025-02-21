# Usa una imagen oficial de Python como base
FROM python:3.9-slim

# Evita la creación de archivos pyc y habilita el modo sin búfer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary peewee python-dotenv

# Variables de entorno para Flask
ENV FLASK_APP=src/app.py
ENV FLASK_ENV=development

# Exponer el puerto 5000 para acceder a la app Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "src/app.py"]
