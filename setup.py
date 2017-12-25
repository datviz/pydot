#!/usr/bin/env python
"""Installation script."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import pydot


long_description = '''
Graphviz's dot language Python interface.

This module provides with a full interface to
create handle modify and process graphs in
Graphviz's dot language.

References:

* pydot Homepage: https://github.com/erocarrera/pydot
* Graphviz:       http://www.graphviz.org/
* DOT Language:   http://www.graphviz.org/doc/info/lang.html

Copyright (c) 2005-2011 Ero Carrera <ero.carrera@gmail.com>

Distributed under MIT license
[http://opensource.org/licenses/mit-license.html].
'''


setup(
    name='pydot',
    version=pydot.__version__,
    description="Python interface to Graphviz's Dot",
    author='Ero Carrera',
    author_email='ero@dkbza.org',
    maintainer='Ioannis Filippidis',
    maintainer_email='jfilippidis@gmail.com',
    url='https://github.com/erocarrera/pydot',
    license='MIT',
    keywords='graphviz dot graphs visualization',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description=long_description,
    py_modules=['pydot', 'dot_parser'],
    install_requires=['pyparsing>=2.1.4'],
    tests_require=['chardet'])
