from django import forms
from .models import DatoCurioso, Comentario, Autor, Categoria

# Formulario para agregar un Dato Curioso
from django import forms
from .models import DatoCurioso

class DatoCuriosoForm(forms.ModelForm):
    class Meta:
        model = DatoCurioso
        fields = ['titulo', 'descripcion', 'categoria', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }


# Formulario para agregar un Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario de búsqueda
class BusquedaForm(forms.Form):
    termino = forms.CharField(label="Buscar", max_length=100)
#formulario autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'profesion']
        widgets = {
            'profesion': forms.TextInput(attrs={'placeholder': 'Ej. Biólogo, Historiador... (opcional)'}),
        }
#formulario categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'profesion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
        }
