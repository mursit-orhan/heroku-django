pip install gunicorn
django-admin startproject core .
django-admin startapp newapp

touch Procfile
touch runtime.txt
python --version

pip install whitenoise
pip install django-crispy-forms

python manage.py collectstatic
pip freeze > requirements.txt


pip install django-environ

docker build -t django-heroku:v1 .
docker run -p 8000:8000 django-heroku:v1
git remote add origin <Remote url>
heroku login
heroku container:login
heroku create
heroku container:push web -a=morning-journey-82108
heroku config:add ALLOWED_HOSTS=* -a morning-journey-82108
heroku config:get ALLOWED_HOSTS -a morning-journey-82108
heroku container:release -a morning-journey-82108 web
heroku logs --tail -a morning-journey-82108
heroku open -a morning-journey-82108


