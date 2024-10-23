#### Video Tutorial of this project
https://youtu.be/SQ4A7Q6_md8
<br><br>

#### Getting the files
Download zip file or <br>
Clone with git + remove git folder
```
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git
```
<br><br><br>

## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
pip install virtualenv 
virtualenv venv 
venv\Scripts\activate.bat 
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```
### - Crear app para administrar los tenants
```bash
django-admin startapp a_tenant_manager
```
### - Crear migraciones despues de configurar el modelo para los tenants
```bash
python manage.py makemigrations
```
### - Ejecutar las migraciones
```bash
python manage.py migrate
```
### - Crear cliente tenant
* En dominio se debe ingresar el subdominio y localhost subdominio.localhost
```bash
python manage.py create_tenant
```
### - Crear superuser para cliente tenant
```bash
python manage.py create_tenant_superuser
```
# Despues de crear un nuevo modelo
```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
                                 --tenant
                                 --schema=tenantname
                                 --executor=parallel
```
## Despues de modificar un modelo
```bash
python manage.py makemigrations
python manage.py migrate
```
## Generar SECRET KEY
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```