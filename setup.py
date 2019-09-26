#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'fourbars',
    version = '0.2.0',
    description = 'Ableton Live CLI - High Precision Loop Production and Asset Management',
    long_description = open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    author = 'Peter Styk',
    author_email = 'dev@4bars.media',
    url = 'https://github.com/styk-tv/4bars',
    packages = ['fourbars'],
    install_requires = [
        'cython==0.29.13',
        'termcolor==1.1.0',
        'live @ git+ssh://git@github.com:ideoforms/pylive.git@cacb9ed69e129f4471d09f7a9548a5a6c5e32f13#egg=live',
        'randomnames @ git+ssh://git@github.com:styk-tv/python-randomnames.git@beaa1fad993bf03ac5bc6f3ace2eaed119585f80#egg=randomnames',
        'yamlordereddictloader==0.4.0',
        'pyliblo >= 0.9.1'
        ],
    keywords = ['sound', 'music', 'ableton', 'osc', 'pylive'],
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
