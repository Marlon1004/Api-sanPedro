# Api-sanPedro

# Sistema de Inscripción de Estudiantes en Prácticas en un Hospital

## Descripción
Este sistema permite a los estudiantes registrarse y solicitar prácticas en un hospital, mientras que la administración del hospital puede aceptar o rechazar dichas solicitudes. El sistema está desarrollado con Django y utiliza MySQL como base de datos.

## Tecnologías Utilizadas
- **Backend:** Django (Python)
- **Base de Datos:** MySQL
- **Frontend:** HTML y CSS
- **Autenticación:** Roles personalizados (Universidad, Hospital)

## Características Principales
1. **Registro y autenticación de usuarios** con diferentes roles.
2. **Perfil de estudiante**, donde pueden gestionar sus solicitudes de prácticas.
3. **Perfil del hospital**, con la capacidad de aceptar o rechazar solicitudes.
4. **Interfaz de usuario sencilla** basada en HTML y CSS.
5. **Gestor de base de datos MySQL** para almacenar información de usuarios y solicitudes.

## Instalación
### Prerrequisitos
- Python 3
- MySQL
- Virtualenv (opcional, pero recomendado)

### Pasos
1. **Clonar el repositorio**
   ```bash
   git clone <repositorio_url>
   cd <nombre_proyecto>
   ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos MySQL**
   - Crear una base de datos en MySQL:
     ```sql
     CREATE DATABASE inscripcion_hospital;
     ```
   - Configurar `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'inscripcion_hospital',
             'USER': 'tu_usuario',
             'PASSWORD': 'tu_contraseña',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear un superusuario** (opcional para acceso administrativo)
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

## Uso del Sistema
- **Estudiantes**: pueden registrarse, iniciar sesión y solicitar prácticas.
- **Hospital**: puede ver solicitudes y aceptarlas o rechazarlas.
- **Administradores**: pueden gestionar usuarios y configuraciones desde el panel de Django Admin.

## Estructura del Proyecto
```
<nombre_proyecto>/
│── manage.py
│── db.sqlite3  (si se usa SQLite en lugar de MySQL)
│── inscripcion_hospital/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│   └── ...
│── apps/
│   ├── estudiantes/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── ...
│   ├── hospital/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── ...
│── templates/
│── static/
└── requirements.txt
