#!/bin/bash -> alpine linux scripts execution
echo "apply database migration"
python manage.py migrate
exec "$@" # exceute command line



