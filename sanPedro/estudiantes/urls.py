from django.urls import path
from .views import registro_estudiante, registro_hospital, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('registro/estudiante/', registro_estudiante, name='registro_estudiante'),
    path('registro/hospital/', registro_hospital, name='registro_hospital'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]
