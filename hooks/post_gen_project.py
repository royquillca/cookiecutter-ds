import subprocess
import os
import sys

# Messages/logs colors
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
virtualenv_name = "{{cookiecutter.virtualenv_name}}"
project_slug = "{{cookiecutter.project_slug}}"

print(f"{MESSAGE_COLOR}Almost done!")

print(f"Creating the virtual enviroment...{RESET_ALL}")
# subprocess.call(["python","-m", "venv", f"{virtualenv_name}"]) # Usando el modulo venv nativo de Python
subprocess.call(["virtualenv", f"{virtualenv_name}"]) # Usando virtual env
print(f"{MESSAGE_COLOR}The virtual environment have been created succesfully.{RESET_ALL}")


# print(f"Accessing the virtual environment {virtualenv_name}...{RESET_ALL}")
# os.system(f"source {virtualenv_name}/Scripts/activate && pip install requirements.txt")
# subprocess.call(["pip","install", "-r", "requirements.txt"])
# print(f"{MESSAGE_COLOR}You are inside the virtual environment {virtualenv_name}!{RESET_ALL}")

# print(f"Installing fundamental/standard libraries for Data Science projects..{RESET_ALL}")
# subprocess.call(["pip","install", "-r", "requirements.txt"])
# print(f"{MESSAGE_COLOR}The libraries have installed succesfully!{RESET_ALL}")

print(f"Initializating a git repository...{RESET_ALL}")
subprocess.call(["git","init"])
subprocess.call(["git","add","*"])
subprocess.call(["git","commit","-m", "Initial commit"])
print(f"{MESSAGE_COLOR}The beginning of your destination is defined now! Create and have fun!{RESET_ALL}")


# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#     return stdout, stderr

# def print_message(message, color=MESSAGE_COLOR):
#     print(f"{color}{message}{RESET_ALL}")

# print_message("Almost done!")

# print_message("Creating the virtual environment...")
# run_command(f"virtualenv {virtualenv_name}")
# print_message("The virtual environment has been created successfully.")

# print_message(f"Accessing the virtual environment {virtualenv_name}...")
# run_command(f"source {virtualenv_name}/Scripts/activate")
# print_message("The virtual environment has been activated.")

# print_message("Installing dependencies...")
# run_command(f"pip install -r requirements.txt")
# print_message("The dependencies have been installed successfully.")