"""
commit to git
"""

import os

message = input("Enter message:")

commands = ['git add .', f"git commit -m {message}", 'git push']

for command in commands:
    os.system(command=command)
