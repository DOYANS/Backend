"""
create package file
"""

import os

cmd = "pip freeze > requirements.txt"

os.system(cmd)
