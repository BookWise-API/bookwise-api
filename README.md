# bookwise-api README Temporário 

Libs instaladas:
pip install djangorestframework ipython drf-spectacular gunicorn black dj-database-url djangorestframework-simplejwt PyJWT whitenoise psycopg2-binary python-dotenv

Comandos Frequentes: 

1. Criar ambiente virtual:
python -m venv venv

2. Ativar o venv:
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate


# Salvar Libs no requirements.txt
pip freeze > requirements.txt
# Instalar Libs do requirements.txt
pip install -r requirements.txt

# Iniciar projeto
django-admin startproject PROJECTNAME .
# Iniciar APP
python manage.py startapp APPNAME

# Migrations:
python manage.py makemigrations

python manage.py migrate
