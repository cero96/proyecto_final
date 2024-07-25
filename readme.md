##ghp_PE5VwZHg6d03HXz           #        sDlRBAm5BsAA3zb0VOQXV##

# Proyecto Final. 


## Objetivos 


## Tareas a realizar


## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL

### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate

~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles

### Iniciar servidor
#### Linux o MaCOS
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación
#### Linux o MaCOS
~~~
python3 manage.py startapp <nombre_de_la_aplicacion>
~~~
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion>
~~~

### Crear Súper Usuario
#### Linux o MaCOS
~~~
python3 manage.py createsuperuser
~~~
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Linux o MaCOS
~~~
python3 manage.py makemigrations
~~~
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Linux o MaCOS
~~~
python3 manage.py migrate
~~~
#### Windows
~~~
python manage.py migrate
~~~

### Almacenar depdendencias y librerías instaladas
#### Linux o MaCOS
~~~
pip3 freeze > requirements.txt
~~~
#### Windows
~~~
pip freeze > requirements.txt
~~~

