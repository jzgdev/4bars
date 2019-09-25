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
from clip import Clip
from cmd import Cmd


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        #sys.stderr.write('ERROR: %s\n' % message)
        print ("""Usage: 4bars (BETA) [-version] [-help] <command> [args]

The available commands for execution are listed below
Commands marked [WIP] are work-in-progress

Common commands:
    cd          [WIP] essential directory navigation
    set         [WIP] set management
    track       [WIP] current track setup
    device      [WIP] device management
    record      [WIP] record all clips on 4BARS_ prefixed track
    sync        [WIP] synchronize exported assets with 4bars.media
    status      [WIP] check if all requirements and communication is working
    login       [WIP] login to 4bars service. obtain api token
""")

        sys.exit(0)


def get_version():
    try:
        return pkg_resources.get_distribution("4bars").version
    except:
        return Cmd.local_run_get_out("get version", "git describe --tags")


def main(args=None):
    description = colored("4bars - (c) 2019 Piotr Styk <dev@4bars.media> - {0}".format(get_version()), 'white', attrs=['bold'])
    parser = MyParser(prog="./4bars.py", description=description, usage=argparse.SUPPRESS, add_help=False)
    parser.add_argument('cd', nargs='+', help='essential directory navigation')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--clip', dest="clip", metavar=('CLIPFILE'), help='create Ableton <clip> from 4bars datafile', action='store')
    group.add_argument('--clip-delete', help='delete clip', action='store_true')

    print()
    print(description)
    args = parser.parse_args()

    if args.clip:
        clip = Clip()
        #clip.add_clip()
        #clip.add_note()
        filename = clip.get_clip()

    elif args.clip_delete:
        pass



if __name__ == "__main__":
    main()
