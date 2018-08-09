#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from setuptools import setup, find_packages
from pip.req import parse_requirements


setup(
    name='funcat2',
    version='0.0.1',
    description='funcat2',
    packages=find_packages(exclude=[]),
    author='Lipson',
    url='https://github.com/Grass-CLP/funcat2',
    author_email='LipsonChan@yahoo.com',
    package_data={'': ['*.*']},
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
)
