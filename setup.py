#!/usr/bin/env python
from setuptools import setup

setup(
    name = 'EIPy',
    version = '0.1',
    author = 'Halcyon Lab',
    description = 'Command-line EIP location tool',
    keywords = 'EIP offset exploit infosec pentest',
    url = 'http://github.com/halcyonlab/eipy',
    entry_points = {
        'console_scripts': ['eipy=EIPy.eipy:main'],
    }
)
