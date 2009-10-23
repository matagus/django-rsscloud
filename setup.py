# -*- coding: utf-8 -*-

"""
A nice example to make setup.py file can be found
at http://jacobian.org/writing/django-apps-with-buildout/
thanks to Jacob Kaplan-Moss.
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-rsscloud",
    version = "0.1.1",
    url = 'http://github.com/matagus/django-rsscloud',
    license = 'BSD',
    description = "Simple app to make rsscloud-enabled your Django app feed.",
    long_description = read('README'),

    author = 'Matias Agustin Mendez',
    author_email = 'me@matagus.com.ar',

    packages = find_packages(),

    install_requires = ['setuptools', 'django'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

