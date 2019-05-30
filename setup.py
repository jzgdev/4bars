#!/usr/bin/env python

from setuptools import setup

setup(
    name = '4bars',
    version = '0.1.0',
    description = 'RESTful API remote control of Ableton Live',
    long_description = open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    author = 'Piotr Styk',
    author_email = 'polfilm@gmail.com',
    url = 'https://github.com/styk-tv/4bars',
    packages = ['4bars'],
    install_requires = ['pyliblo >= 0.9.1', 'cython'],
    keywords = ('sound', 'music', 'ableton', 'osc','pylive'),
    classifiers = [
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Artistic Software',
        'Topic :: Communications',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-timeout']
)
