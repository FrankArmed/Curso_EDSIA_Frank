# Imagen de pythonnnn
FROM python:3.12-slim

# Esto evita archivos .pyc y muestra los logs sin retraso.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo.
WORKDIR /app

# Se copian las dependencias.
COPY requirements.txt .

# Instala las dependencias sin guardar la caché de pip.
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación.
COPY app ./app

# Copia la configuración y las migraciones de la base de datos.
COPY alembic.ini .
COPY migrations ./migrations

# Documenta el puerto utilizado por FastAPI.
EXPOSE 8000

# Aplica las migraciones y después inicia la API.
# PORT viene de Render; localmente se utiliza 8000.
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]