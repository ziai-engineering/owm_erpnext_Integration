# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='openweather_integration',
    version=version,
    description='Openweathermap.org',
    author='Brandon Fox, Foxtrot',
    author_email='bfox@foxtrot.email',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
