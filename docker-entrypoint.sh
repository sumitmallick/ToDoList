#!/bin/sh
python manage.py db upgrade

exec gunicorn -w 2 -b :5000 --reload manage:app