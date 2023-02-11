import os
import sys
import re

project_slug = "{{cookiecutter.project_slug}}"
ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_aLL = "\x1b[0m"

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
# module_name = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, project_slug):
    print('ERROR: %s is not a valid Python module name!' % project_slug)
    # exits with status 1 to indicate failure
    sys.exit(1)

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug} is not valid for this template.{RESET_aLL}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at {os.getcwd()}{RESET_aLL}")