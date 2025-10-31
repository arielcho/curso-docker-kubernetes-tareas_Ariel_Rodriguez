
# Clase 1 - Introducción a Containers y Docker

El objetivo principal de esta primera práctica es comprender los fundamentos de Docker, ejecutar los primeros contenedores, explorar imágenes oficiales desde Docker Hub y aprender los comandos básicos para gestionarlos. Además, se debe desplegar un contenedor con Apache HTTP Server para observar cómo funciona un servicio dentro de un contenedor y familiarizarse con su ciclo de vida.

Un contenedor es un proceso aislado que incluye todo lo necesario para ejecutar una aplicación: código, dependencias, librerías y configuraciones. A diferencia de una máquina virtual, un contenedor no necesita un sistema operativo completo, ya que comparte el kernel con el host, lo que lo hace más ligero y rápido.

Docker se compone de los siguientes elementos:
- Docker Engine: servicio que administra y ejecuta los contenedores.
- Imágenes (Images): plantillas inmutables que definen una aplicación.
- Contenedores (Containers): instancias activas de una imagen.
- Docker Hub: repositorio público de imágenes oficiales.

---

## Parte práctica – Despliegue de Apache HTTP Server

### Aplicación elegida
httpd (Apache HTTP Server)

### 1. Crear y ejecutar el contenedor
```bash
docker run -d --name tarea1 -p 8081:80 httpd:2.4
````

Explicación rápida:

* `-d`: ejecuta en segundo plano (detached)
* `--name tarea1`: nombre del contenedor
* `-p 8081:80`: mapea puerto local 8081 → puerto 80 del contenedor
* `httpd:2.4`: imagen oficial de Apache 2.4

### 2. Verificar su funcionamiento

Para confirmar que el contenedor funciona correctamente se ejecutaron los siguientes comandos:

```bash
docker ps
docker logs tarea1
curl http://localhost:8081/
```

Resultados esperados:

* `docker ps` muestra el contenedor **tarea1** en ejecución con el puerto 8081 publicado.
* `docker logs tarea1` muestra los registros de inicio de Apache (incluyendo solicitudes GET).
* Al abrir **[http://localhost:8081/](http://localhost:8081/)** en el navegador (o con `curl`) se visualiza la página por defecto de Apache con el mensaje **"It works!"**.

### 3. Detener y eliminar el contenedor

Una vez verificado el servicio, se procede a detener y eliminar el contenedor para dejar el entorno limpio:

```bash
docker stop tarea1
docker rm tarea1
docker ps
```

Explicación:

* `docker stop tarea1`: detiene el contenedor en ejecución.
* `docker rm tarea1`: elimina el contenedor detenido.
* `docker ps`: confirma que ya no hay contenedores activos.

---

## Comandos adicionales útiles

```bash
docker images             # listar imágenes
docker ps -a              # listar contenedores, incluidos detenidos
docker inspect tarea1     # detalles del contenedor (si está presente)
docker history httpd:2.4  # historial de capas de la imagen
docker stats              # uso de CPU/RAM/red en tiempo real
docker image prune -a     # eliminar imágenes no utilizadas
docker logs -f tarea1     # logs en tiempo real (si está en ejecución)
```

---

## Evidencias

Guardar capturas en `clase1/screenshots/`:

* `docker-ps.png` → contenedor en ejecución
* `navegador-8081.png` → “It works!” en el navegador
* `limpieza.png` → `stop`, `rm` y `docker ps` sin el contenedor

Estructura sugerida:

```
clase1/
├── README.md
└── screenshots/
    ├── docker-ps.png
    ├── navegador-8081.png
    └── limpieza.png
```

---

## Conclusiones

1. Se ejecutó con éxito un contenedor de Apache HTTP Server desde la imagen oficial `httpd:2.4`.
2. Se verificó el servicio accediendo a `http://localhost:8081/` y revisando los logs del contenedor.
3. Se practicó el ciclo de vida completo del contenedor: crear, verificar, detener y eliminar.
4. Se reforzó el uso de mapeo de puertos, nombres de contenedor y lectura de logs como herramientas de control.
5. El entorno quedó limpio y listo para continuar con las siguientes tareas del curso.

```

