#!/bin/bash

python3 manage.py collectstatic --noinput &&
python3 manage.py makemigrations metro_app users &&
python3 manage.py migrate &&
python3 manage.py runserver 0.0.0.0:8000
