#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import django_mathjax

setup(
    name = 'django-mathjax',
    version = "0.0.8",
    description = "MathJax easy integration with django",
    long_description = "",
    keywords = 'django, mathjax',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/kaleidos/django-mathjax',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
