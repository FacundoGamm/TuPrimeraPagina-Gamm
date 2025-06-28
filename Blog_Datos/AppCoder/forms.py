from django import forms
from .models import DatoCurioso, Comentario

# Formulario para agregar un Dato Curioso
class DatoCuriosoForm(forms.ModelForm):
    class Meta:
        model = DatoCurioso
        fields = ['titulo', 'descripcion', 'categoria', 'autor']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
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
