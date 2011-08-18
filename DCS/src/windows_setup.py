from distutils.core import setup
import py2exe
import os
import sys
DCS_path = os.path.abspath("./gui") 
sys.path.append(DCS_path)
DCS_path = os.path.abspath("./utils") 
sys.path.append(DCS_path) 
print sys.path


main_path = os.path.join("gui", "main.py")
lib_path = os.path.join("utils", "build", "libutils.dll")

setup(
    name="DCS v0.1a",
    version="0.1a",
    description = "Dynamic Camouflage System",
    author="Stanislav Bobovych",
    author_email="stan.bobovych@gmail.com",
    windows = [
          {'icon_resources': [(0, 'dcs.ico')], 'dest_base': 'DCS', 'script': main_path}
    ],
    data_files = [(lib_path)]
)
