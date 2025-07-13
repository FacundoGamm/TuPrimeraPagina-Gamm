from django.shortcuts import render, redirect, get_object_or_404
from .models import DatoCurioso, Comentario, Categoria, Autor
from .forms import DatoCuriosoForm, ComentarioForm, BusquedaForm, AutorForm, CategoriaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

#--------------------------------------------------------------------------

def inicio(request):
    datos_usuario = None
    if request.user.is_authenticated:
        datos_usuario = DatoCurioso.objects.filter(autor=request.user)

    return render(request, "AppCoder/inicio.html", {
        "datos_usuario": datos_usuario,
    })

#--------------------------------------------------------------------------

def lista_datos(request):
    datos = DatoCurioso.objects.all()
    return render(request, "AppCoder/datosCuriosos.html", {"datos": datos})
#--------------------------------------------------------------------------

def detalle_dato(request, dato_id):
    dato = get_object_or_404(DatoCurioso, id=dato_id)
    comentarios = dato.comentarios.all()

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.dato = dato
            comentario.save()
            return redirect("detalle_dato", dato_id=dato.id)
    else:
        form = ComentarioForm()

    return render(request, "AppCoder/detalle_dato.html", {
        "dato": dato,
        "comentarios": comentarios,
        "form": form
    })
#-------------------------------------------------------------------------
@login_required
def agregar_dato(request):
    if request.method == "POST":
        form = DatoCuriosoForm(request.POST)
        if form.is_valid():
            dato = form.save(commit=False)
            dato.autor = request.user  # Asignar automáticamente el usuario logueado
            dato.save()
            return redirect("lista_datos")
    else:
        form = DatoCuriosoForm()

    return render(request, "AppCoder/formulario/agregar_dato.html", {"form": form})

#--------------------------------------------------------------------------

def nuevo_comentario(request, dato_id):
    dato = get_object_or_404(DatoCurioso, id=dato_id)
    
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.dato = dato
            comentario.save()
            return redirect("detalle_dato", dato_id=dato.id)
    else:
        form = ComentarioForm()

    return render(request, "AppCoder/nuevo_comentario.html", {"form": form, "dato": dato})
#-------------------------------------------------------

def buscar_datos(request):
    form = BusquedaForm(request.GET or None)
    resultados = []

    if form.is_valid():
        termino = form.cleaned_data["termino"]
        resultados = DatoCurioso.objects.filter(titulo__icontains=termino)

    return render(request, "AppCoder/buscar_datos.html", {
        "form": form,
        "resultados": resultados
    })

#-------------------------------------------------------
def ver_autores(request):
    autores = Autor.objects.all()
    return render(request, "AppCoder/autores.html", {"autores": autores})
#-------------------------------------------------------
def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "AppCoder/categorias.html", {"categorias": categorias})

# ---------------------------------------------------
@login_required
def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_autores")
    else:
        form = AutorForm()
    return render(request, "AppCoder/formulario/autor_form.html", {"form": form})

# ---------------------------------------------------
@login_required
def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_categorias")
    else:
        form = CategoriaForm()
    return render(request, "AppCoder/formulario/categoria_form.html", {"form": form})

#----------------------------------------------------
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()

            # Crear un Autor relacionado con el usuario registrado
            Autor.objects.create(nombre=usuario.username)

            login(request, usuario)
            messages.success(request, "¡Registro exitoso! Bienvenido.")
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, "AppCoder/registro.html", {"form": form})

#----------------------------------------------------
#edición de datos creados
@login_required
def editar_dato(request, dato_id):
    dato = get_object_or_404(DatoCurioso, id=dato_id)
    if request.method == "POST":
        form = DatoCuriosoForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            messages.success(request, "Dato actualizado correctamente.")
            return redirect("detalle_dato", dato_id=dato.id)
    else:
        form = DatoCuriosoForm(instance=dato)
    return render(request, "AppCoder/formulario/editar_dato.html", {"form": form, "dato": dato})

# ---------------------------------------------------
#opción de eliminar dato
@login_required
def eliminar_dato(request, dato_id):
    dato = get_object_or_404(DatoCurioso, id=dato_id)
    if request.method == "POST":
        dato.delete()
        messages.success(request, "Dato eliminado.")
        return redirect("lista_datos")
    # plantilla de confirmación
    return render(request, "AppCoder/confirmar_eliminar.html", {"dato": dato})
