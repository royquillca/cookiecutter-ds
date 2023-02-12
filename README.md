# Cookiecutter for Data Science Projects

_A powerful and user-friendly Cookiecutter template for Data Science projects._

## Requirements

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create a new project

In a folder where you want your generate your project:

```bash
cookiecutter https://github.com/royquillca/cookiecutter-ds
```

## Demo

<a href="https://www.youtube.com/watch?v=HQxNCA0gZ7E" target="_blank">
  <img src="https://img.youtube.com/vi/HQxNCA0gZ7E/0.jpg" alt="demo-video-thumbnail-added">
</a>

## Resulting directory structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── Installation.md    <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description
    │   └── 0.0-example-data-exploratory.ipynb  <- Example notebook ready to be used as script
    │   └── 1.0-{{cookiecutter.project_author_name}}-data-cleaning.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-data-exploration.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-data-preprocessing.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-feature-selection.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-model-training.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-model-evaluation-and-optimization.ipynb                        
    │   └── 2.0-{{cookiecutter.project_author_name}}-monitoring-and-maintenance.ipynb   
    │            
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so {{ cookiecutter.project_module_name }} can be imported.
    │
    └── {{ cookiecutter.project_module_name }}               <- Source code for use in this project. Default src/
        ├── __init__.py    <- Makes {{ cookiecutter.project_module_name }} a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py

## Contributing guide

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## Credits

This project is heavily influenced by [drivendata's Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science), [andfanilo's Cookiecutter for Kaggle Conda projects](https://github.com/andfanilo/cookiecutter-kaggle), and julia's package [DrWatson](https://juliadynamics.github.io/DrWatson.jl/dev/).

Other links that helped shape this cookiecutter :

- [Write less terrible code with Jupyter Notebook](https://blog.godatadriven.com/write-less-terrible-notebook-code)
- [Cookiecutter DataScience Opinions](http://drivendata.github.io/cookiecutter-data-science/#opinions)