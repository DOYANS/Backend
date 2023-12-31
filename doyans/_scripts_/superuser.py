"""
CREATE SUPERUSER
"""

import os

CMD = "python manage.py createsuperuser"

os.system(CMD)
