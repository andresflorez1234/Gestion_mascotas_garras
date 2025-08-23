from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Tipo, Persona
from .forms import TipoForm, PersonaForm, UsuarioForm
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

def crear_persona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personas")
    else:
        form = PersonaForm()
    return render(request, "aplicacion_garras/persona_form.html", {"form": form, "action": "Crear"})


def editar_persona(request, id_persona):
    persona = get_object_or_404(Persona, id_persona=id_persona)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect("personas")
    else:
        form = PersonaForm(instance=persona)
    return render(request, "aplicacion_garras/persona_form.html", {"form": form, "action": "Editar"})


def eliminar_persona(request, id_persona):
    persona = get_object_or_404(Persona, id_persona=id_persona)
    if request.method == "POST":
        persona.delete()
        return redirect("personas")
    return render(request, "aplicacion_garras/persona_confirm_delete.html", {"persona": persona})


# usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "aplicacion_garras/usuarios.html", {"usuarios": usuarios})

def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm()
    return render(request, "aplicacion_garras/usuario_form.html", {"form": form, "action": "Crear"})

def editar_usuario(request, id_persona, id_tipo):
    usuario = get_object_or_404(Usuario, id_persona=id_persona, id_tipo=id_tipo)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "aplicacion_garras/usuario_form.html", {"form": form, "action": "Editar"})

def eliminar_usuario(request, id_persona, id_tipo):
    usuario = get_object_or_404(Usuario, id_persona=id_persona, id_tipo=id_tipo)
    if request.method == "POST":
        usuario.delete()
        return redirect("usuarios")
    return render(request, "aplicacion_garras/usuario_confirm_delete.html", {"usuario": usuario})

# redirecciones a las paginas
def home(request):
    return render(request, 'aplicacion_garras/home.html')


