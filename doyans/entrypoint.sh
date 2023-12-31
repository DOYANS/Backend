#!/bin/ash
echo "apply database migration"
python manage.py makemigrations
python manage.py migrate
exec "$@"
