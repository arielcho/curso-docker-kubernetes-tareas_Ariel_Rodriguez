"# Clase 1 - Tarea Docker" 
#  Clase 1 – Introducción a Containers y Docker

##  Objetivo de la clase
Comprender los **fundamentos de Docker**, ejecutar los **primeros contenedores**, explorar las **imágenes oficiales** y practicar comandos esenciales.  
Además, desplegar una aplicación simple (**Apache HTTP Server**) para familiarizarse con el ciclo de vida de un contenedor.

---

##  Contexto teórico
### ¿Qué es un contenedor?
Un contenedor es un **proceso aislado** que ejecuta una aplicación con todas sus dependencias, compartiendo el kernel del sistema operativo.  
A diferencia de una máquina virtual, **no requiere un sistema operativo completo**, por lo que es más liviano, rápido y eficiente.

###  Componentes principales de Docker
| Componente | Descripción |
|-------------|-------------|
| **Docker Engine** | Servicio que ejecuta y administra contenedores. |
| **Imagen (Image)** | Plantilla inmutable (*read-only*) que define qué ejecutará el contenedor. |
| **Contenedor (Container)** | Instancia en ejecución de una imagen. |
| **Docker Hub** | Repositorio público de imágenes oficiales. |

---

## Parte práctica – Despliegue de Apache HTTP Server

###  Aplicación elegida
**httpd (Apache HTTP Server)**

---

###  Comandos ejecutados

####  1. Crear y ejecutar el contenedor
```bash
docker run -d --name tarea1 -p 8081:80 httpd:2.4

#### 2. Verificar su funcionamiento
Para confirmar que el contenedor funciona correctamente se ejecutaron los siguientes comandos:

```bash
docker ps
docker logs tarea1
curl http://localhost:8081/

#### 3. Detener y eliminar el contenedor
Una vez verificado el funcionamiento del contenedor, se procede a detenerlo y eliminarlo para completar el ciclo de vida del contenedor y mantener limpio el entorno.

Los comandos utilizados fueron:

```bash
docker stop tarea1
docker rm tarea1
docker ps

Explicación:

docker stop tarea1: detiene el contenedor que está en ejecución.

docker rm tarea1: elimina el contenedor detenido del sistema.

docker ps: permite confirmar que el contenedor ya no aparece en la lista de contenedores activos.

Este proceso garantiza que no queden contenedores en ejecución ni recursos ocupados innecesariamente.

Conclusiones

Se comprendió el funcionamiento general de Docker y su arquitectura basada en imágenes y contenedores.

Se ejecutó con éxito un contenedor de Apache HTTP Server utilizando la imagen oficial httpd:2.4 desde Docker Hub.

Se verificó que el servicio Apache respondió correctamente mostrando la página “It works!”, confirmando que el contenedor estaba operativo.

Se aplicaron correctamente los comandos básicos para crear, ejecutar, inspeccionar, detener y eliminar contenedores.

Se evidenció la facilidad y rapidez con la que Docker permite desplegar servicios aislados sin depender de configuraciones complejas.

Se reforzó la comprensión del mapeo de puertos, nombres de contenedor y visualización de logs como herramientas esenciales de control.

Se finalizó la tarea con el entorno limpio, comprendiendo el ciclo completo del contenedor (creación, ejecución, verificación, eliminación).

El entorno quedó correctamente configurado en Ubuntu WSL2 + Docker Desktop, listo para continuar con la siguiente clase del curso Docker & Kubernetes.