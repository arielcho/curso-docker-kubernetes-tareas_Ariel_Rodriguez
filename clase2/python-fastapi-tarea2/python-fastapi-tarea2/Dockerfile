
# ===========================
# Stage 1: Build Dependencies
# ===========================
FROM python:3.12-slim AS build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instalar build deps mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar solo dependencias primero (mejor cache)
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip wheel --wheel-dir=/wheels -r requirements.txt

# ===========================
# Stage 2: Runtime
# ===========================
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

# Crear usuario no-root
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Instalar solo las ruedas (runtime)
COPY --from=build /wheels /wheels
RUN pip install --no-index --find-links=/wheels /wheels/* && rm -rf /wheels

# Copiar código fuente
COPY app ./app

# Metadatos (labels)
LABEL org.opencontainers.image.title="tarea2-fastapi" \
      org.opencontainers.image.description="API FastAPI de ejemplo para Tarea 2 (multi-stage)" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.vendor="Curso Docker"

# Exponer puerto (documentación)
EXPOSE 8000

# Healthcheck (opcional pero recomendado)
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -fsS http://localhost:${PORT}/api/health || exit 1

# Cambiar a usuario no-root
USER appuser

# Comando por defecto
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
