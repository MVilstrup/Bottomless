"""Sphinx configuration."""
project = "Bottomless"
author = "Mikkel Vilstrup"
copyright = "2022, Mikkel Vilstrup"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
