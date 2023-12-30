"""
database management
"""

import os

commands = [
'python manage.py makemigrations', 
' python manage.py makemigrations api ', 
' python manage.py makemigrations accounts ', 
' python manage.py makemigrations data ',
' python manage.py makemigrations dashboard ',
' python manage.py makemigrations worker ', 
' python manage.py migrate',
]

for command in commands:
    os.system(command)
