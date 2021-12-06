release: cd myapi && python3 manage.py makemigrations
release: cd myapi && python3 manage.py migrate
web: cd myapi && gunicorn myapi.wsgi