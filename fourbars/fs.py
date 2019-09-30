import argparse
from cmd_parser import CommandParser
from locations import Locations
import os
import sys

class Fs(object):

    parser = None
    subars = None
    locations = None

    def __init__(self, in_subargs):
        self.locations = Locations()

        self.parser = CommandParser(
            usage=argparse.SUPPRESS,
            add_help=False)

        # some fs names have dashes
        if len(in_subargs) > 1:
            if "-" in in_subargs[1]:
                in_subargs[1] = in_subargs[1].replace('-', '_')

        self.subargs = in_subargs

        # if single (this) subarg, then only help
        if len(self.subargs) < 2:
            self.parser.help_fs()
            return

        self.parser.add_argument('fs', help='Subcommand to run')

        args = self.parser.parse_args(in_subargs[1:2])

        if not hasattr(self, args.fs):
            self.parser.help_fs()
            exit(1)

        getattr(self, args.fs)()

        pass

    def help(self):
        self.parser.help_fs()

    def list_tracks(self):
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ['Name', '# Tracks', 'Tempo', 'Beats']
        table.align = "l"

        from mido import MidiFile
        files = [os.path.join(self.locations.pwd,f) for f in os.listdir(self.locations.pwd) if os.path.isfile(os.path.join(self.locations.pwd,f)) and f.lower().endswith(('.mid'))]

        import pretty_midi
        for f in files:
            pmid = pretty_midi.PrettyMIDI(f)

#            print (f)
            mid = MidiFile(f)
            path_array = f.split('/')
            file_name = path_array[len(path_array)-1]
            table.add_row([file_name, len(mid.tracks), pmid.get_end_time(), ""])
            # iterate through tracks
#            for i, track in enumerate(mid.tracks):
#                print('Track {}: {}'.format(i, track.name))

#                #for msg in track:
#                #    print(msg)

        print(table)
        print()




#    def prefs(self):
#        print(Locations().get_fullpretty())

