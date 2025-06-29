from django.shortcuts import render, redirect, get_object_or_404
from .models import DatoCurioso, Comentario, Categoria, Autor
from .forms import DatoCuriosoForm, ComentarioForm, BusquedaForm, AutorForm, CategoriaForm
#--------------------------------------------------------------------------

def inicio(request):
    return render(request, "AppCoder/inicio.html")
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
def agregar_dato(request):
    if request.method == "POST":
        form = DatoCuriosoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_datos")
    else:
        form = DatoCuriosoForm()

    return render(request, "AppCoder/agregar_dato.html", {"form": form})
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
def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_categorias")
    else:
        form = CategoriaForm()
    return render(request, "AppCoder/formulario/categoria_form.html", {"form": form})
