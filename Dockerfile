# Usa una imagen base de Python ligera
FROM python:3.9-slim-buster

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de tu proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que utiliza tu aplicación (puerto 8000 en este ejemplo)
EXPOSE 8000

# Comando para ejecutar el servidor de FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]