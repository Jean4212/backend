# Imagen base para FastAPI
FROM python:3.9 AS base

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

# Imagen base para PostgreSQL
FROM postgres:latest AS postgres_base

# Variables de entorno para PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Imagen final que combina FastAPI y PostgreSQL
FROM base AS final

# Instala el cliente de PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Copia la configuración de PostgreSQL desde la imagen base
COPY --from=postgres_base / /

# Comando de inicio para ejecutar la aplicación FastAPI y PostgreSQL
CMD ["bash", "-c", "service postgresql start && uvicorn app:app --host 0.0.0.0 --port 8000"]
