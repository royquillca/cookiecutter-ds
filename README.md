# Tutorial de Cookiecutter

Configuracion del archivo ``cookiecutter.json``:

```json
{
    "project_title": "Cookiecutter Personal",
    // Reemplazo de espacios y "-" por "_". Jinja funciona igual que Python.
    "project_slug": "{{ cookiecutter.project_title.lower().replace(' ', '_').replace('-','_') }}",
    "project_description":  "Add description",
    "project_author_name": "Your name",
    "project_packages": ["All", "Minimal"],
    "python_version": "3.7.9",
    "project_license": ["MIT"],
    "virtualenv_name": "venv"
}
```

## Implementación de Hooks

Cosas que se van ajecutar antes y despues de generar la plantilla. Para ello crearemos la carpeta ``hooks`` al nivel de la carpeta ``{{cookiecutter.project_Slug}}`` que contendrá dos archivos python  ``pre_gen_project.py`` y ``post_gen_project.py`` en los cuales indicaremos que acciones se va ha realizar antes y después de generar la plantilla, respectivamente.

## Distribucion de Plantilla del Proyecto

