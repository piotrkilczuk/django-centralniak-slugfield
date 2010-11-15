#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-centralniak-slugfield',
    version='0.1.3',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'Provides more handy support for slugs in models',
    packages=find_packages(),
    provides=['django_centralniak_slugfield'],
    classifiers=[
        'Framework :: Django',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
