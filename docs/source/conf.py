# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import tomllib
from datetime import datetime
from os.path import abspath, dirname, join

cwd = dirname(abspath(__file__))
root = join(cwd, "../..")

sys.path.insert(0, root)

toml_file = join(root, "pyproject.toml")

now = datetime.now()

project = "NUmPyGIS"


def parse_authors(authors_section: list[dict[str, str]]) -> str:
    authors = []
    for author in authors_section:
        if "name" not in author:
            raise ValueError("Author name not present")
        if "email" in author and author["email"]:
            authors.append(f"{author['name']} <{author['email']}>")
            continue
        authors.append(author["name"])
    return ", ".join(authors)


with open(toml_file, "rb") as f:
    data: dict = tomllib.load(f)
    project_section = data["project"]
    if not isinstance(project_section, dict):
        raise ValueError("`project` is not present in toml.")

    if "version" not in project_section:
        raise ValueError("`version` not in project")
    version = project_section["version"]

    if "authors" not in project_section:
        raise ValueError("`author` not in project")

    authors_section = project_section["authors"]
    name = project_section["name"]
    authors = parse_authors(authors_section=authors_section)

copyright = f"{now.year}, {authors}"
release = version
author = authors

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
