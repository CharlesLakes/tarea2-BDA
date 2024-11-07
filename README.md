
# Tarea 2

Esta tarea corresponde a la **Tarea 2** del ramo **Base de Datos Avanzadas**. El objetivo de la tarea es configurar un **Replica Set** de MongoDB utilizando Docker y migrar datos a una base de datos de MongoDB. Los comandos necesarios están disponibles a través de `make` para facilitar la ejecución de los diferentes pasos.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos:

- Docker
- Docker Compose
- Python 3
- MongoDB (para ejecutar el Replica Set)
- `make` (para gestionar los comandos de construcción)
- El archivo `games.json` (con los datos a migrar). Puedes descargarlo desde el siguiente enlace:  
  [Descargar `games.json`](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset?resource=download)

### Instalación de dependencias de Python

El proyecto utiliza la librería `pymongo` para interactuar con MongoDB. Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

Este comando instalará `pymongo` y cualquier otra dependencia definida en el archivo `requirements.txt`.

## Instrucciones de uso

### 1. Levantar los contenedores de Docker

Para iniciar los contenedores de Docker, que contienen las instancias de MongoDB, ejecuta:

```bash
make docker
```

Este comando levanta los contenedores definidos en el archivo `docker-compose.yml` en segundo plano. Asegúrate de que todos los contenedores de MongoDB estén en funcionamiento.

### 2. Iniciar el Replica Set

Después de crear la base de datos, debes inicializar el Replica Set en MongoDB. Para ello, ejecuta:

```bash
make replica
```

Este comando ejecuta el script `init-replica-set.sh`, que configura el Replica Set de MongoDB para garantizar la redundancia de los datos entre las instancias.

### 3. Migrar los datos

El siguiente paso es migrar los datos a la base de datos `Steam` en MongoDB. Para ello, ejecuta el siguiente comando:

```bash
make migrate
```

Este comando ejecuta el script `migrate_data.py`, que toma los datos del archivo `games.json` y los inserta en la colección `Games` de la base de datos `Steam`. Si la colección `Games` ya existe, será eliminada antes de insertar los nuevos datos.

### 4. Conexión a MongoDB

Para conectarte a uno de los nodos del Replica Set, puedes usar la siguiente URI de conexión:

```bash
mongodb://[ip-contenedor]/?replicaSet=myReplicaSet&directConnection=true
```

Donde **[ip-contenedor]** es la IP de uno de los contenedores que están ejecutando MongoDB.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```
/project
│
├── Makefile               # Archivo de comandos de make
├── docker-compose.yml     # Archivo de configuración de Docker Compose
├── games.json             # Archivo con los datos de los juegos (descargar desde Kaggle)
├── init-replica-set.sh    # Script para inicializar el Replica Set
├── migrate_data.py        # Script de migración de datos
├── requirements.txt       # Archivo con las dependencias de Python
```

## Comandos de Make

El proyecto incluye un archivo `Makefile` que define los siguientes comandos:

- **docker**: Levanta los contenedores de Docker.
- **replica**: Inicializa el Replica Set.
- **migrate**: Ejecuta la migración de datos.
```
