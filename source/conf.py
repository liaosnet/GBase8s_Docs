# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# import sphinx_pdj_theme

project = 'GBase 8s数据库 文档'
copyright = '2025, GBASEDBT.COM'
author = 'liaosnet'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
    'sphinx_markdown_tables',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_static']
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'
html_search_language = 'zh'
html_show_sphinx = False
html_show_sourcelink = False
# html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
html_theme_options = {'logo_only': True}
