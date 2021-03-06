# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- 设置主题 -----------------------------------------------------
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- 支持markdown编写 -----------------------------------------------------
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

from recommonmark.transform import AutoStructify

github_doc_root = 'https://github.com/ldsxp/xadmin-py3/tree/master/docs/'


# app setup hook
def setup(app):
    app.add_config_value('xadmin_config', {
        # 'url_resolver': lambda url: github_doc_root + url,  # 将文档中现有相对位置映射到http链接的函数
        # 'auto_toc_tree_section': 'Contents',  # 当为True时，仅在与标题匹配的部分启用Auto Toc Tree
        # 'enable_eval_rst': True,  # 启用评估嵌入式reStructuredText功能
        # 'enable_auto_doc_ref': True,  # 启用Auto Doc Ref功能。弃用
    }, True)

    app.add_transform(AutoStructify)


# -- 其他自定义设置 -----------------------------------------------------

# 要使用的 Pygments（语法高亮）样式的名称。
pygments_style = 'sphinx'

# -- Project information -----------------------------------------------------

project = 'docs_example'
copyright = '2020, lds'
author = 'lds'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.viewcode', 'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
language = 'zh_CH'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
