from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Agrega campos personalizados si es necesario
    pass

    

from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    universidad = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db import models

from django.db import models

class Hospital(models.Model):
    nombre = models.CharField(max_length=255)  # Asegúrate de que el nombre coincida
    correo = models.EmailField()
    universidad = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre




class SolicitudPractica(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Solicitud de {self.estudiante} a {self.hospital} - {self.estado}"
