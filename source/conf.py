from datetime import datetime
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Documentation Template'
copyright = '2025, Naxior'
author = 'Naxior'
release = 'latest'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_multiversion',
]

templates_path = ['_templates']
exclude_patterns = []

version = 'latest'
release = 'latest'

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_templates_path = ['_templates']
html_css_files = [
    'css/custom.css',
]
html_js_files = [
    'js/custom.js',
]
html_sidebars = {
    "**": [
        "versions.html",
    ],
}
html_favicon = '_static/img/favicon.ico'
html_logo = '_static/img/logo.png'
html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

# SPHINX MULTIVERSION
smv_tag_whitelist = r"^\d+\.\d+\.\d+$|^latest$|^test$"
smv_branch_whitelist = None
smv_released_pattern = r"^refs/tags/.*$"
smv_prefer_remote_refs = False
smv_outputdir_format = "{ref.name}"

# SPHINX I18N
gettext_compact = False

