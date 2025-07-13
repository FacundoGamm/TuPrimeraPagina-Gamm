from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('datos/', views.lista_datos, name='lista_datos'),

    path('datos/<int:dato_id>/', views.detalle_dato, name='detalle_dato'),

    path('datos/nuevo/', views.agregar_dato, name='agregar_dato'), 

    path('comentario/<int:dato_id>/nuevo/', views.nuevo_comentario, name='nuevo_comentario'),

    path('autores/', views.ver_autores, name='ver_autores'),  #al poner /autores se ve la lista de autores cargadso

    path('categorias/', views.ver_categorias, name='ver_categorias'),#al poner /categorias se ve la lista

    path('buscar/', views.buscar_datos, name='buscar_datos'),

    path('autores/nuevo/', views.agregar_autor, name='agregar_autor'), #/autores/nuevo - para crear autor

    path('categorias/nuevo/', views.agregar_categoria, name='agregar_categoria'),#/categorias/nuevo - para crear una categoría

    path('registro/', views.registro, name='registro'),

    path('datos/<int:dato_id>/editar/', views.editar_dato, name='editar_dato'),
    
    path('datos/<int:dato_id>/eliminar/', views.eliminar_dato, name='eliminar_dato'),

]
