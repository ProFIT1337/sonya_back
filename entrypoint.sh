#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/usr/src/app/