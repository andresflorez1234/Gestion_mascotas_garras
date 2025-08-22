from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Tipo, Persona
from .forms import TipoForm
from django.contrib import messages

# Create your views here.

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(usuario=username, pass_field=password)
            return redirect('inicio')
        except Usuario.DoesNotExist:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, 'aplicacion_garras/ingreso.html', {'error': error})

from django.contrib.auth import logout as django_logout
def logout(request):
    request.session.flush()
    return redirect('home')


# cargos
def lista_cargos(request):
    tipos = Tipo.objects.all()
    return render(request, "aplicacion_garras/cargos.html", {"tipos": tipos})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tipo, Persona
from .forms import TipoForm

def lista_cargos(request):
    tipos = Tipo.objects.all()
    return render(request, "aplicacion_garras/cargos.html", {"tipos": tipos})


def agregar_cargo(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cargos")
    else:
        form = TipoForm()
    return render(request, "aplicacion_garras/cargo_form.html", {"form": form, "accion": "Agregar"})

def editar_cargo(request, pk):
    cargo = get_object_or_404(Tipo, pk=pk)
    if request.method == "POST":
        form = TipoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            messages.success(request, "Cargo modificado correctamente")
            return redirect("cargos")
    else:
        form = TipoForm(instance=cargo)
    return render(request, "aplicacion_garras/cargo_form.html", {"form": form, "accion": "Editar"})

def eliminar_cargo(request,pk):
    cargo = get_object_or_404(Tipo, pk=pk)
    if request.method == "POST":
        cargo.delete()
        return redirect("cargos")
    return render(request, "aplicacion_garras/confirmar_eliminar.html", {"cargo": cargo})


# personas
def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, "aplicacion_garras/personas.html", {"personas": personas})



# usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "aplicacion_garras/usuarios.html", {"usuarios": usuarios})


# redirecciones a las paginas
def home(request):
    return render(request, 'aplicacion_garras/home.html')


