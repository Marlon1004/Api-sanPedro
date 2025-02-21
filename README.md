# Api-sanPedro
https://api-sanpedro.onrender.com/
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



## 3. Detalle de la Implementación

### 3.1 Modelos (`models.py`)
- **Estudiante:**
  ```python
  class Estudiante(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      nombre = models.CharField(max_length=255)
      universidad = models.CharField(max_length=255)
      correo = models.EmailField(unique=True)
  ```

- **Hospital:**
  ```python
  class Hospital(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      nombre = models.CharField(max_length=255)
      direccion = models.CharField(max_length=255)
  ```

- **SolicitudPráctica:**
  ```python
  class SolicitudPractica(models.Model):
      estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
      hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
      estado = models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], max_length=10)
  ```

### 3.2 Rutas (`urls.py`)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('solicitudes/', views.lista_solicitudes, name='solicitudes'),
    path('aprobar/<int:id>/', views.aprobar_solicitud, name='aprobar_solicitud'),
    path('rechazar/<int:id>/', views.rechazar_solicitud, name='rechazar_solicitud'),
]
```

### 3.3 Vistas (`views.py`)
- **Registro de Usuarios:**
  ```python
  def registro(request):
      if request.method == 'POST':
          form = RegistroForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('login')
      else:
          form = RegistroForm()
      return render(request, 'registro.html', {'form': form})
  ```

- **Inicio de Sesión:**
  ```python
  def login_view(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              return redirect('solicitudes')
      return render(request, 'login.html')
  ```

- **Lista de Solicitudes:**
  ```python
  def lista_solicitudes(request):
      solicitudes = SolicitudPractica.objects.all()
      return render(request, 'solicitudes.html', {'solicitudes': solicitudes})
  ```

### 3.4 Plantillas HTML (`templates/`)
- **registro.html:** Formulario de registro con campos de usuario y contraseña.
- **login.html:** Formulario de autenticación con opción de recordar sesión.
- **solicitudes.html:** Listado de solicitudes de práctica con botones para aceptar o rechazar.

## 4. Decisiones Claves
- **Uso de MySQL** en lugar de SQLite para mejor escalabilidad.
- **Implementación de roles personalizados** para seguridad y control.
- **Creación de migraciones** desde el inicio para un manejo eficiente de la base de datos.
- **Separación de módulos** en aplicaciones Django para mejorar la organización del código.
- **Estructura clara de directorios** siguiendo las mejores prácticas de Django.
