"""Sphinx configuration."""
from datetime import datetime


project = "Yet Another Python Styleguide"
author = "Alex Vakhitov"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]
html_static_path = ["_static"]
