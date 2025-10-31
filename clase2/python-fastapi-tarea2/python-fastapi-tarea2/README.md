
# Clase 2 - Dockerización (FastAPI + Multi-Stage)

## Aplicación
**Lenguaje:** Python 3.12  
**Framework:** FastAPI + Uvicorn  
**Descripción:** API REST minimal con endpoints de salud y gestión simple de ítems.

**Endpoints:**
- `GET /` → mensaje de bienvenida
- `GET /api/health` → healthcheck (usado por `HEALTHCHECK` de Docker)
- `GET /api/items` → lista de ítems (en memoria)
- `POST /api/items` → crear ítem (en memoria)

Puerto configurable por env var `PORT` (por defecto **8000**).

---

## Dockerfile (Multi-Stage)

```dockerfile
# Stage 1: build (genera ruedas en /wheels)
FROM python:3.12-slim AS build
...
# Stage 2: runtime (usuario no-root, healthcheck, labels)
FROM python:3.12-slim AS runtime
...
```

### Buenas prácticas aplicadas
- Multi-stage: build deps separadas del runtime
- Imagen base ligera (`python:3.12-slim`)
- Usuario **no-root** (`appuser`)
- `EXPOSE 8000` y `HEALTHCHECK` → `/api/health`
- `.dockerignore` para reducir el build context
- Variables de entorno (`PORT`)

---

## .dockerignore
Excluye `.git`, `__pycache__`, virtualenvs, `.env`, etc.

---

## Construcción (Build)
```bash
# Estando en el directorio del proyecto
docker build -t fastapi-tarea2:1.0 .
```

Ver tamaño de la imagen:
```bash
docker images fastapi-tarea2
```

---

## Ejecución y Pruebas Locales
```bash
# Ejecutar en segundo plano publicando el puerto 8000
docker run -d --name fastapi-tarea2 -p 8000:8000 fastapi-tarea2:1.0

# Probar endpoints
curl http://localhost:8000/
curl http://localhost:8000/api/health
curl http://localhost:8000/api/items
curl -X POST http://localhost:8000/api/items -H "Content-Type: application/json" -d '{"id":3,"name":"Ruler","price":1.2}'
```

Ver logs:
```bash
docker logs fastapi-tarea2
```

---

## Publicar en Docker Hub
```bash
# 1) Login
docker login

# 2) Tag (reemplaza USUARIO por tu usuario de Docker Hub)
docker tag fastapi-tarea2:1.0 USUARIO/fastapi-tarea2:1.0

# 3) Push
docker push USUARIO/fastapi-tarea2:1.0
```

Luego entra a Docker Hub y verifica que el repo sea **público**.

---

## Optimizaciones sugeridas
- Probar un stage final aún más pequeño con `python:3.12-alpine` 
- Usar `--mount=type=cache` con BuildKit para cache de pip
- Congelar dependencias con versiones exactas
- Analizar capas con:
```bash
docker history fastapi-tarea2:1.0
```

---

## Conclusiones (plantilla)
- Aprendí a separar entornos de *build* y *runtime* para reducir tamaño y mejorar seguridad.
- Implementé usuario **no-root** y *healthcheck*.
- Publicar en Docker Hub me permite distribuir la imagen fácilmente.
