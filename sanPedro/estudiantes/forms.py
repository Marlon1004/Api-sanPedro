from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Estudiante, Hospital

class EstudianteRegistroForm(UserCreationForm):
    codigo = forms.CharField(max_length=20)
    carrera = forms.CharField(max_length=100)
    universidad = forms.CharField(max_length=100)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = 'estudiante'
        if commit:
            user.save()
            Estudiante.objects.create(
                usuario=user,
                codigo=self.cleaned_data['codigo'],
                carrera=self.cleaned_data['carrera'],
                universidad=self.cleaned_data['universidad']
            )
        return user

class HospitalRegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=255)
    direccion = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = 'hospital'
        if commit:
            user.save()
            Hospital.objects.create(
                usuario=user,
                nombre=self.cleaned_data['nombre'],
                direccion=self.cleaned_data['direccion']
            )
        return user


from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'correo', 'universidad', 'ciudad', 'telefono']
