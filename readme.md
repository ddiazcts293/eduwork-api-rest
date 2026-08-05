# EduWork API rest

Este es el repositorio para el proyecto del servidor API rest usando Django Rest Framework.

> [!IMPORTANT]
> Para implementar la autenticación y gestión de usuario es necesario volver a clonar el repositorio, iniciar un nuevo entorno virtual de Python y eliminar la base de datos anteriormente creada.

## Descripción

El proyecto desarrollado consiste en una plataforma web denominada EduWork, orientada a estudiantes universitarios que buscan oportunidades laborales, prácticas profesionales y vacantes de medio tiempo.

El objetivo principal de la plataforma es facilitar la conexión entre estudiantes y empresas mediante una plataforma sencilla, organizada y fácil de utilizar.

## Instalación

**Componentes requieridos:**

- Git
- Python 3.14 & pip
- Docker Compose

**Pasos:**

1. Clonar este repositorio `git clone https://github.com/ddiazcts293/eduwork-api-rest.git`.
2. Inicializar un nuevo entorno virtual de Python en el directorio del proyecto `python -m venv .venv` (usar `py` en Windows).
3. Instalar dependencias `pip install -r requirements.txt`.
4. Orquestar servicios con Docker `docker compose up -d`.
6. Aplicar migraciones con `python manage.py migrate` (dentro del directorio `eduwork_backend`).
7. Poblar BD con datos iniciales usando `python manage.py loaddata api_rest/fixtures/initial_data.json`.
8. Crear superusuario con `python manage.py createsuperuser`.
9. Iniciar servidor web con `python manage.py runserver`.

El sitio es accesible a través del localhost en el puerto 8000; Adminer, puerto 8081.

**URLs:**

- Django Admin: `http://localhost:8000/admin/`
- Swagger: `http://localhost:8000/swagger/`
- Redoc: `http://localhost:8000/redoc/`
