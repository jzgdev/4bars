#!/usr/bin/env python
"""
MIT License

Copyright (c) 2019 Piotr Styk <polfilm@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import argparse
import sys
from cmd_parser import CommandParser
import pkg_resources
from termcolor import colored
from clip import Clip
from cmd import Cmd







class FourBars(object):
    def __init__(self):

        parser = CommandParser(
            usage=argparse.SUPPRESS,
            add_help=False)

        parser.add_argument('command', help='Subcommand to run')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            parser.help_root()
            exit(1)

        getattr(self, args.command)()

    def cd(self):
        from cd import Cd
        cd = Cd(sys.argv[1:])

    def fetch(self):
        parser = argparse.ArgumentParser(
            description='Download objects and refs from another repository')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('repository')
        args = parser.parse_args(sys.argv[2:])
        print('Running git fetch, repository=%s' % args.repository)


if __name__ == "__main__":
    FourBars()
