# Blog Personal de Turismo

Se trata de una web de Turismo, donde el usuario puede loguearse e ir cargando los Sitios, Restaurantes y Monumentos que ha visitado para compartir con sus amigos.

## Instrucciones para ejecutar este proyecto

1. Crear una carpeta en tu computadora
2. Abrirla desde Visual Studio Code
3. Ir a la parte superior de los menús: `Terminal > Nueva terminal`
4. Ejecutar:
```bash
git clone <url_del_repositorio> .
```
5. Instalar los requerimientos del proyecto
```bash
pip install -r requirements.txt
```
6. Crear las migraciones
```bash
python manage.py makemigrations
```
7. Ejecutar las migraciones
```bash
python manage.py migrate
```
8. Ejecutar servidor de Django
```bash
python manage.py runserver
```

Una vez inicializad el blog, podrás visitar la url de [Inicio](http://127.0.0.1:8000/) y comenzar a cargar tus aventuras :) 
