# Imagen base para FastAPI
FROM python:3.9

# Copia los archivos de la aplicación al contenedor
COPY app.py /app/
COPY requirements.txt /app/

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 para la aplicación FastAPI
EXPOSE 8000

# Comando de inicio para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

