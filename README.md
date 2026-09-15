# Entorno Docker para aprender Python 🐍

Un setup mínimo con dos formas de trabajar: Jupyter (interactivo) y Python clásico (scripts).

## Estructura

```
aprender-python/
├── docker-compose.yml
├── notebooks/     ← tus notebooks .ipynb (se crea al levantar Jupyter)
└── scripts/       ← tus archivos .py
    └── hola.py
```

## Cómo levantarlo

```bash
docker compose up -d
```

## Usar Jupyter Notebook (recomendado para empezar)

Abre en tu navegador: <http://localhost:8888>

Token de acceso: **`aprender`**

Todo lo que guardes dentro de la carpeta `work` en Jupyter aparecerá en `./notebooks` de tu computadora.

## Ejecutar scripts de Python

Los archivos en `./scripts/` están montados dentro del contenedor. Para correr uno:

```bash
docker compose exec python python hola.py
```

O entra a una shell interactiva de Python:

```bash
docker compose exec python python
```

O al bash del contenedor (para instalar librerías con `pip`, etc.):

```bash
docker compose exec python bash
```

## Instalar librerías

Dentro del contenedor `python`:

```bash
pip install requests pandas numpy
```

> ⚠️ Estas instalaciones se pierden si recreas el contenedor. Cuando avances,
> te conviene crear un `Dockerfile` con un `requirements.txt`.

## Detener todo

```bash
docker compose down
```
