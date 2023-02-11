import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
virtualenv_name = "{{cookiecutter.virtualenv_name}}"

print(f"{MESSAGE_COLOR}Almost done!")

print(f"Creating the virtual enviroment...{RESET_ALL}")
subprocess.call(["virtualenv", f"{virtualenv_name}"])
print(f"{MESSAGE_COLOR}The virtual environment have been created succesfully.{RESET_ALL}")

print(f"Installing fundamental/standard libraries for Data Science projects..{RESET_ALL}")
subprocess.call(["pip","install", "-r", "requirements.txt"])
print(f"{MESSAGE_COLOR}The libraries have installed succesfully!{RESET_ALL}")

print(f"Initializating a git repository...{RESET_ALL}")
subprocess.call(["git","init"])
subprocess.call(["git","add","*"])
subprocess.call(["git","commit","-m", "Initial commit"])
print(f"{MESSAGE_COLOR}The beginning of your destination is defined now! Create and have fun!{RESET_ALL}")