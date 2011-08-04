from distutils.core import setup
import py2exe

setup(
      {'icon_resources': [(0, 'dcs.ico')], 'script': 'GUI/main.py'}
)