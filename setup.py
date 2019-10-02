#!/usr/bin/env python

from setuptools import setup
import subprocess
import sys
import pkg_resources
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_semantic_version():
    global VERSION

    proc1 = subprocess.Popen("git describe --tags", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = proc1.communicate()

    if proc1.returncode != 0:
        sys.stdout.write("fourbars must install from cloned folder. make sure .git folder exists\n")
        sys.stdout.write(out[1])
        raise SystemExit(32)

    v = out[0].decode('ascii').replace('\n', '')

    if v.startswith('v.'):
        v = v[2:]
    elif v.startswith('v'):
        v = v[1:]
    li = v.split('.')
    lii = li[1].split('-')
    if len(lii) == 3:
        v = '{0}.{1}.{2}'.format(li[0],lii[0],lii[1])
    else:
        v = '{0}.{1}'.format(li[0], li[1])
    return v


VERSION = get_semantic_version()

setup(
    name = 'fourbars',
    version = VERSION,
    description = 'Ableton Live CLI - High Precision Loop Production and Asset Management',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Peter Styk',
    author_email = 'dev@4bars.media',
    url = 'https://github.com/styk-tv/4bars',
    packages = ['fourbars'],
    install_requires = [
        'Cython==0.29.13',
        'pyliblo >= 0.9.1',
        'termcolor==1.1.0',
        'randomnames@git+https://github.com/styk-tv/python-randomnames.git@beaa1fad993bf03ac5bc6f3ace2eaed119585f80#egg=randomnames',
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
    ]
)
