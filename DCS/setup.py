#!/usr/bin/env python

import glob
import os
from distutils.core import setup, Extension

setup(name='DCS',
      version='0.1',
      description='Dynamic Cammoflauge System',
      author='Stanislav Bobovych',
      author_email='stan.bobovych@gmail.com',
      url='http://sites.google.com/site/sbobovyc/',      
      packages=glob.glob(os.path.join('src')),
      ext_modules=[Extension('DCS.utils', ['DCS/utils.cpp'], libraries=['noise'])]
     )



