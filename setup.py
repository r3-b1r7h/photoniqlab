# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name = 'photoniqlab',
    version = '1.0',
    description = 'An open-source object-oriented Python framework for simulating photonic quantum information processing (PQIP) experiments',
    license = "Apache-2.0",
    author = 'QUANTA',
    author_email = 'junjiewu@nudt.edu.cn',
    packages = find_packages(),
    install_requires = ["sympy", "numpy", "matplotlib"]
    )