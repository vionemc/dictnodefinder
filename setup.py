# This file is part of Dictnodefinder.
#
# Copyright (C) 2020 Aminah Nuraini.
#
# Dictnodefinder is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dictnodefinder is a library that helps you to diff and patch dictionaries."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open('README.rst').read()

extras_require = {
    'docs': [
        'Sphinx>=1.4.4',
        'sphinx-rtd-theme>=0.1.9',
    ]
}

extras_require['all'] = []
for key, reqs in extras_require.items():
    if ':' == key[0]:
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'setuptools_scm>=3.1.0',
]

packages = find_packages()

version_template = """\
# -*- coding: utf-8 -*-
# Do not change the format of this next line. Doing so risks breaking
# setup.py and docs/conf.py
\"\"\"Version information for dictnodefinder package.\"\"\"

__version__ = {version!r}
"""

setup(
    name='dictnodefinder',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': os.path.join('dictnodefinder', 'version.py'),
        'write_to_template': version_template,
    },
    description=__doc__,
    long_description=readme,
    author='Aminah Nuraini',
    author_email='aminah.nuraini92@gmail.com',
    version='1.0',
    url='https://github.com/vionemc/dictnodefinder',
    project_urls={
        'Changelog': (
            'https://github.com/vionemc/dictnodefinder'
            '/blob/master/CHANGES'
        ),
    },
    packages=['dictnodefinder'],
    zip_safe=False,
    extras_require=extras_require,
    setup_requires=setup_requires,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
)
