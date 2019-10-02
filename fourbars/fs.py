import argparse
from parser_cmd import ParserCmd
from parser_track import ParserTrack
from locations import Locations
import os
import sys
from mido import MidiFile
from prettytable import PrettyTable



class Fs(object):

    parser = None
    subars = None
    locations = None
    parsed = None

    def __init__(self, in_subargs):
        self.locations = Locations()

        self.parser = ParserCmd(
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
        self.parser.add_argument('-d', action="store")

        self.parsed = self.parser.parse_args(in_subargs[1:])

        if not hasattr(self, self.parsed.fs):
            self.parser.help_fs()
            exit(1)

        getattr(self, self.parsed.fs)()

        pass

    def help(self):
        self.parser.help_fs()

    def get_mid_files(self):
        files = [os.path.join(self.locations.pwd,f) for f in os.listdir(self.locations.pwd) if os.path.isfile(os.path.join(self.locations.pwd,f)) and f.lower().endswith(('.mid'))]
        if len(files) == 0:
            print ("No .mid files")
            exit(0)

        return files

    def tracks(self):

        if self.parsed.d:
            self.locations.pwd = self.parsed.d

        files = self.get_mid_files()

        import mido
        #import pretty_midi
        from prettytable import PrettyTable

        table = PrettyTable()
        table.field_names = ['Name', '# Tracks', 'Track Name', 'Length (s)', 'Type', 'TicksPerBeat']
        table.align = "l"

        for f in files:

            mid = mido.MidiFile(f)

            path_array = f.split('/')
            file_name = path_array[len(path_array)-1]

            for i, track in enumerate(mid.tracks):
                #ptrack = ParserTrack(track)
                table.add_row([file_name, len(mid.tracks), track.name, mid.length, mid.type, mid.ticks_per_beat ])

        print(table)
        print()

    def notes(self):

        if self.parsed.d:
            self.locations.pwd = self.parsed.d

        files = self.get_mid_files()

        table = PrettyTable()
        table.field_names = ['File', 'Track', 'TicksPerBeat', 'Sig']
        table.align = "l"
        for f in files:

            mid = MidiFile(f)
            path_array = f.split('/')
            file_name = path_array[len(path_array)-1]

            for i, track in enumerate(mid.tracks):
                ptrack = ParserTrack(track)
                table.add_row([file_name, ptrack.name, mid.ticks_per_beat, ptrack.time_signature])








        #print(table)
        #print()


        #pmid = pretty_midi.PrettyMIDI(f)
        #pmid.get_piano_roll(self)
        #for i in pmid.instruments:
        #    roll = i.get_piano_roll(1)
        #    chroma = i.get_chroma()
        #    for n in i.notes:
        #        pass

#    def prefs(self):
#        print(Locations().get_fullpretty())


            #table.add_row([file_name, len(mid.tracks), pmid.get_end_time(), ""])

#            pmid.get_piano_roll(self)
#            for i, track in enumerate(mid.tracks):
#                print('Track {}: {}'.format(i, track.name))
#                pmid.instruments
#                for msg in track:
#                    print(msg)



#    def tracks_old(self):

#        files = self.get_mid_files()

#        import mido
#        import pretty_midi
#        from prettytable import PrettyTable

#        table = PrettyTable()
#        table.field_names = ['Name', '# Tracks', 'Tempo', 'Beats']
#        table.align = "l"
#        for f in files:
#            pmid = pretty_midi.PrettyMIDI(f)

#            print (f)
#            mid = mido.MidiFile(f)

#            path_array = f.split('/')
#            file_name = path_array[len(path_array)-1]
#            table.add_row([file_name, len(mid.tracks), pmid.get_end_time(), ""])
# iterate through tracks
#            for i, track in enumerate(mid.tracks):
#                print('Track {}: {}'.format(i, track.name))

#                #for msg in track:
#                #    print(msg)

#        print(table)
#        print()