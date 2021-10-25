release: python manage.py makemigrations restapi
release: python manage.py migrate

web: gunicorn --chdir ./backend hyperlearner_restful.wsgi
