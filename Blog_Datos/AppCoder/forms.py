from django import forms
from .models import DatoCurioso, Comentario, Autor, Categoria


class DatoCuriosoForm(forms.ModelForm):
    class Meta:
        model = DatoCurioso
        fields = ['titulo', 'descripcion', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }



# Formulario para agregar un Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'comentario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# Formulario de búsqueda
class BusquedaForm(forms.Form):
    termino = forms.CharField(
        label="Buscar",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )


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
