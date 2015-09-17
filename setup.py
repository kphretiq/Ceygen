#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Matěj Laitl <matej@laitl.cz>
# Distributed under the terms of the GNU General Public License v2 or any
# later version of the license, at your option.
from setuptools import setup, find_packages
from os.path import dirname, join
import multiprocessing

from Cython.Build import cythonize
import numpy as np

from support.dist import CeygenDistribution

with open(join(dirname(__file__),'README.rst')) as readme_file:
    long_description = readme_file.read()

setup(
    packages=find_packages(),
    distclass=CeygenDistribution,
    ext_modules=cythonize(['ceygen/*.pyx', 'ceygen/tests/*.pyx'],
                          language='c++', nthreads=multiprocessing.cpu_count()),
    include_dirs=['/usr/include/eigen3'],  # default overridable by setup.cfg
    cflags=['-O2', '-march=native', '-fopenmp'],  # ditto
    ldflags=['-fopenmp'],  # ditto
    install_requires=['Cython>=0.22', 'numpy'],
    test_suite='nose.collector',
    tests_require=['nose'],
    name='Ceygen',
    version="0.4-pre",
    author='Matěj Laitl',
    author_email='matej@laitl.cz',
    maintainer='Matěj Laitl',
    maintainer_email='matej@laitl.cz',
    url='https://github.com/strohel/Ceygen',
    description='Cython helper for linear algebra with typed memoryviews built atop the Eigen C++ library',
    long_description=long_description,
    download_url='http://pypi.python.org/pypi/Ceygen',
    platforms='cross-platform',
    license='GNU GPL v2+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
