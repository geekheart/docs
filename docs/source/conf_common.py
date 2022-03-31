from local_util import run_cmd_get_output, copy_if_modified
import sys
import os
import re
import subprocess
import shlex
import recommonmark
from recommonmark.transform import AutoStructify

sys.setrecursionlimit(3500)


version = run_cmd_get_output('git describe')

release = version

exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

extensions = ['link-roles',
              'recommonmark',
              'sphinx_markdown_tables'
              ]

templates_path = ['_templates']

html_logo = "../_static/wireless-tag.jpg"

html_static_path = ['../_static' '_static']

html_js_files = ['baidu_analytics.js', ]


def setup(app):
    app.add_css_file('theme_overrides.css')
