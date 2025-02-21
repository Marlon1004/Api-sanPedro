from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Estudiante, Hospital, SolicitudPractica

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')  # Se eliminó 'rol' si no existe

admin.site.register(Usuario, UsuarioAdmin)

# Agregar clases admin básicas para evitar errores
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'universidad', 'ciudad', "telefono")  # Ajusta según tu modelo

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')  # Ajusta según tu modelo

@admin.register(SolicitudPractica)
class SolicitudPracticaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'hospital', 'estado')  # Ajusta según tu modelo
