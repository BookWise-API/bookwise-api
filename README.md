<a href="https://insomnia.rest/run/?label=BookWise%20API&uri=https%3A%2F%2Fgithub.com%2FBookWise-API%2Fbookwise-api%2Fblob%2Fmain%2FBookWise_InsomniaProject" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

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
