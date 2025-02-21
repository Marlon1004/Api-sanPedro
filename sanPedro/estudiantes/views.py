from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import EstudianteRegistroForm, HospitalRegistroForm

def registro_estudiante(request):
    if request.method == 'POST':
        form = EstudianteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = EstudianteRegistroForm()
    return render(request, 'estudiantes/registro_estudiante.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Hospital
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Hospital  # Asegúrate de importar el modelo adecuado


def estudiante_view(request):
    return render(request, "estudiante.html")  # 👈 Aquí debe estar tu plantilla de estudiantes


def registro_hospital(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre_completo")  # Si el formulario envía "nombre_completo"
        
        # Asegurar que coincide con el modelo
        Hospital.objects.create(
            nombre=nombre,  # 👈 Aquí debe ser "nombre" porque es el campo en el modelo
            correo=request.POST.get("correo"),
            universidad=request.POST.get("universidad"),
            direccion=request.POST.get("direccion"),
            telefono=request.POST.get("telefono")
        )

        return redirect("estudiante")  # Redirigir después del registro

    return render(request, "estudiantes/registro_hospital.html")




def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'estudiantes/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')







from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Estudiante
from .forms import EstudianteForm

def registrar_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # Enviar respuesta AJAX
        return JsonResponse({"success": False, "errors": form.errors})
    
    estudiantes = Estudiante.objects.all()
    form = EstudianteForm()
    return render(request, 'registro_estudiante.html', {'form': form, 'estudiantes': estudiantes})

