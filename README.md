Asesorías
=============
> "La educación es la única posibilidad de una revolución sin sangre, no violenta y en profundidad de nuestra cultura y nuestros valores."  — Fernando Savater


#### _Correr el proyecto_

```
$ export COMPOSE_FILE=local.yml

$ docker-compose build
$ docker-compose up

$ docker-compose ps

$ docker rm -f asesorias_django_1
$ docker-compose run --rm --service-ports django

$ docker-compose down
```

#### _Hacer migraciones en la base de datos_
```
$ docker volume ls
$ docker volume rm asesorias_local_postgres_data
$ docker-compose run --rm django python manage.py makemigrations
$ docker-compose run --rm django python manage.py migrate
```

#### _Crear superusuarios_
```
$ docker-compose run --rm django python manage.py createsuperuser
```

#### _Abrir consola interactiva de python_
```
$ docker-compose run --rm django python manage.py shell_plus
```

#### _Subir registros de escuelas desde un archivo CSV a la DB_
1. Abre la consola interactiva de python (comando de arriba)
```
$ docker-compose run --rm django python manage.py shell_plus
```
2. Importa la función load_schools
```
$ from asesorias.utils.csv_loader import load_schools
```
3. Llama a la función pasando como argumento el nombre del archivo
```
$ load_schools('asesorias/utils/res/schools.csv')
```
