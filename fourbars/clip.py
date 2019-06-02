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


import live
import os
import yaml
import yamlordereddictloader

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Clip(object):

    set = None
    track = None
    clip = None

    def __init__(self):

        self.debug_set_access()
        self.debug_track_access_assume_first_is_midi()

        self.add_clip()
        self.debug_clip_access()

    def debug_set_access(self):
        self.set = live.Set()
        self.set.scan(scan_clip_names = True, scan_devices = True)
        self.set.tempo = 110.0

    def debug_track_access_assume_first_is_midi(self):
        self.track = self.set.tracks[0]
        print("Track name %s" % self.track.name)

    def debug_clip_access(self):
        # only if clip exists
        self.clip = self.track.clips[0]
        print("Clip name %s, length %d beats" % (self.clip.name, self.clip.length))

    def play(self):
        self.clip.play()

    def add_clip(self):
        self.set.create_clip(0, 0, 8)

        # since references by value not ref, we need to reload
        self.debug_set_access()
        self.debug_track_access_assume_first_is_midi()

    def add_note(self):
        example_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ex001.4bars.yaml")
        data = None
        if os.path.isfile(example_file):
            data = yaml.load(open(example_file), Loader=yamlordereddictloader.Loader)


        print (data)
        # note position duration velocity
        self.clip.add_note(60, 0, 0.25, 60)
        self.clip.add_note(60, 1, 0.25, 10)
        self.clip.add_note(60, 2, 0.25, 120)
        self.clip.add_note(61, 3, 1, 120)

