#!/usr/bin/env python

# Todo list to prepare a release:
#  - set VERSION: faulthandler.c, setup.py, doc/conf.py, doc/index.rst
#  - update the changelog: doc/index.rst
#  - run tests with run tox
#  - run tests on Linux, Windows, FreeBSD and Mac OS X:
#    test at least Python 2.7
#  - set release date in the changelog: doc/index.rst
#  - git commit -a
#  - git tag -a faulthandler-x.y -m "tag version x.y"
#  - git push
#  - git push --tags
#  - python setup.py register sdist upload
#  - Build 32-bit and 64-bit wheel packages on Windows:
#
#    - python2.6 setup.py bdist_wheel upload
#    - python2.7 setup.py bdist_wheel upload
#    - python3.1 setup.py bdist_wheel upload
#    - python3.2 setup.py bdist_wheel upload
#
#  - update the website
#
# After the release:
#  - increment VERSION: faulthandler.c, setup.py, doc/conf.py, doc/index.rst
#  - git commit -a
#  - git push

from __future__ import with_statement
try:
    # setuptools supports bdist_wheel
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
from os.path import join as path_join
import sys

if sys.version_info >= (3, 3):
    print("ERROR: faulthandler is a builtin module since Python 3.3")
    sys.exit(1)

VERSION = "2.5"

FILES = ['faulthandler.c', 'traceback.c']

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Debuggers',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

with open('README') as f:
    long_description = f.read().strip()

options = {
    'name': "faulthandler",
    'version': VERSION,
    'license': "BSD (2-clause)",
    'description': 'Display the Python traceback on a crash',
    'long_description': long_description,
    'url': "http://faulthandler.readthedocs.org/",
    'author': 'Victor Stinner',
    'author_email': 'victor.stinner@gmail.com',
    'ext_modules': [Extension('faulthandler', FILES)],
    'classifiers': CLASSIFIERS,
}

setup(**options)

