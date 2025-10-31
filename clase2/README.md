# Clase 2 - Dockerización de Aplicación con Multi-Stage Build (FastAPI)

##  Descripción de la Aplicación

**Lenguaje:** Python 3.12  
**Framework:** FastAPI + Uvicorn  
**Descripción:**  
API REST minimalista que implementa operaciones básicas en memoria para demostrar **multi-stage builds** y buenas prácticas de contenedorización en Docker.

**Endpoints implementados:**
| Método | Ruta | Descripción |
|:------:|:-----|:-------------|
| `GET` | `/` | Mensaje de bienvenida |
| `GET` | `/api/health` | Endpoint de *healthcheck* |
| `GET` | `/api/items` | Lista los ítems actuales |
| `POST` | `/api/items` | Crea un nuevo ítem en memoria |

**Puerto configurable:** variable de entorno `PORT` (por defecto `8000`).

---

##  Dockerfile Multi-Stage

### Estructura general
El proyecto utiliza un **multi-stage build** con dos etapas:

```dockerfile
# Stage 1: build
FROM python:3.12-slim AS build
...
# Stage 2: runtime
FROM python:3.12-slim AS runtime
...
````

###  Explicación de cada etapa

| Etapa       | Propósito                                             | Detalles                                                                                      |
| :---------- | :---------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Build**   | Instalar dependencias y generar *wheels* en `/wheels` | Mejora el caché y evita instalar compiladores en el contenedor final                          |
| **Runtime** | Ejecutar la aplicación de manera ligera y segura      | Solo incluye las *wheels*, usa usuario **no-root**, expone puerto 8000 y define `HEALTHCHECK` |

###  Buenas prácticas aplicadas

* Multi-stage para separar *build* / *runtime*
* Imagen base ligera `python:3.12-slim`
* Usuario **no-root** (`appuser`)
* `EXPOSE 8000` y `HEALTHCHECK /api/health`
* `.dockerignore` para reducir contexto
* Labels OCI con metadata

---

## Proceso de Build

**Comando ejecutado:**

```bash
docker build -t fastapi-tarea2:1.0 .
```

**Salida resumida:**

```
exporting to image
naming to docker.io/library/fastapi-tarea2:1.0
Successfully tagged fastapi-tarea2:1.0
```

**Verificación de tamaño:**

```bash
docker images fastapi-tarea2
```

---

## Testing Local

###  Ejecución del contenedor

```bash
docker run -d --name fastapi-tarea2 -p 8000:8000 fastapi-tarea2:1.0
```

Verificación:

```bash
docker ps
```


---

### Pruebas de endpoints

```bash
curl http://localhost:8000/
curl http://localhost:8000/api/health
curl http://localhost:8000/api/items
curl -X POST http://localhost:8000/api/items \
     -H "Content-Type: application/json" \
     -d '{"id":3,"name":"Ruler","price":1.2}'
```


###  Logs de la aplicación

```bash
docker logs fastapi-tarea2 --tail=50
```
`Uvicorn running on http://0.0.0.0:8000`

---





## Optimizaciones y análisis de capas

```bash
docker history fastapi-tarea2:1.0
```

### Resumen de optimizaciones

* Multi-stage → redujo tamaño significativamente
* Dependencias separadas del runtime
* `.dockerignore` evita archivos innecesarios
* Usuario no-root y *healthcheck* mejoran seguridad
* Imagen reproducible y portable

---

## 7️ Conclusiones

* Logré **dockerizar una aplicación FastAPI** aplicando multi-stage builds correctamente.
* Separar etapas de *build* y *runtime* redujo el tamaño y aumentó la seguridad.
* Entendí la importancia del **orden de instrucciones** para aprovechar el caché.
* Añadí buenas prácticas como `.dockerignore`, `HEALTHCHECK` y usuario no-root.
* Publiqué la imagen en **Docker Hub**, cumpliendo con todos los requisitos de la Tarea 2.

