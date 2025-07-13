
Este proyecto es un blog de datos curiosos. Permite explorar una variedad de datos curiosos subidos por otros usuarios. Es necesario estar logueado para poder publicar un dato, editarlo, comentar, etc. El autor de cada dato es el usuario logueado en ese momento. Al estar logueado, en el inicio se mostrarán los datos publicados por el usuario, así como también se puede buscar sobre todos los datos por palabra/palarabras clave. Se tiene la posibilidad de editar o eliminar los datos publicados y de salir de la sesión.
## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/FacundoGamm/TuPrimeraPagina-Gamm.git
cd TuPrimeraPagina-Gamm/Blog_Datos


2. Crear y activar entorno virtual:
python -m venv venv
venv\Scripts\activate    

3. Instalar dependencias:
pip install -r requirements.txt

4. Migrar base de datos
python manage.py migrate

# Usuario: PruebaFinal // Contraseña: Contraseña123 (Ultimo usuario creado con su publicación correspondiente)
python manage.py runserver
