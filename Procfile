release: python backend/manage.py makemigrations restapi
release: python backend/manage.py migrate

web: gunicorn --chdir ./backend hyperlearner_restful.wsgi
