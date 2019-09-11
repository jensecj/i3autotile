import sys
from setuptools import setup

version = sys.version_info[:2]
if version < (3, 7):
    print('i3autotile requires Python version 3.7 or later' + ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

setup(name='i3autotile',
      version='0.1.0',
      description='Simple window splitting',
      url='http://github.com/jensecj/i3autotile',
      author='Jens Christian Jensen',
      author_email='jensecj@gmail.com',
      packages=['i3autotile'],
      entry_points = {
          'console_scripts': ['i3autotile = i3autotile.i3autotile:main'],
      },
      zip_safe=False)
