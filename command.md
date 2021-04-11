pip install gunicorn
django-admin startproject core .
django-admin startapp newapp

touch Procfile
touch runtime.txt
python --version

pip install whitenoise

python manage.py collectstatic
pip freeze > requirements.txt