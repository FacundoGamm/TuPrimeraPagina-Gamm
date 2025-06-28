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
]
