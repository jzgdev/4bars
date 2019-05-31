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
import pkg_resources
from termcolor import colored
from fourbars.clip import Clip


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        #sys.stderr.write('ERROR: %s\n' % message)
        #self.print_help()
        sys.exit(2)


def get_version():
    try:
        return pkg_resources.get_distribution("4bars").version
    except:
        return "git based version"
        #return Cmd.local_run_get_out("get version", "git describe --tags")


def main(args=None):
    description = colored("4bars {0} - (c) 2019 Piotr Styk".format(get_version()), 'white', attrs=['bold'])
    parser = MyParser(prog="./4bars.py", description=description)
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-c', '--clip', dest="clip", metavar=('CLIPFILE'), help='create Ableton <clip> from 4bars datafile', action='store')
    group.add_argument('--clip-delete', help='delete clip', action='store_true')

    args = parser.parse_args()

    if not len(sys.argv) > 1:
        print()
        print(description)
        print

    args = parser.parse_args()
    #sett = settings.Settings(args)

    if args.clip:
        clip = Clip()
        clip.add_note()

    elif args.clip_delete:
        pass


if __name__ == "__main__":
    main()
