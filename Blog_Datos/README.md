
Este proyecto es un blog de datos curiosos. Permite a los usuarios explorar curiosidades, clasificarlas por categorías, comentar y consultar información sobre los autores.

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

python manage.py runserver
