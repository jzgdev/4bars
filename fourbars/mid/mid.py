
import os
import mido
from prettytable import PrettyTable
from fourbars.alive.locations import Locations
from fourbars.alive.parser_track import ParserTrack


class Mid(object):

    parser = None
    locations = None
    sub_args = None
    pretty_table = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        self.locations = Locations()

    def get_mid_files(self):
        files = [os.path.join(self.locations.pwd,f) for f in os.listdir(self.locations.pwd) if os.path.isfile(os.path.join(self.locations.pwd,f)) and f.lower().endswith(('.mid'))]
        if len(files) == 0:
            print ("No .mid files")
            exit(0)

        return files

    def tracks(self):

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        files = self.get_mid_files()

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

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        files = self.get_mid_files()

        for f in files:

            mid = mido.MidiFile(f)
            path_array = f.split('/')
            file_name = path_array[len(path_array)-1]

            pretty_table = PrettyTable()
            pretty_table.field_names = ['Name', 'Value']
            pretty_table.align = "l"
            pretty_table.add_row(["File Name", file_name])
            pretty_table.add_row(["MIDI Type", mid.type])
            pretty_table.add_row(["# Tracks", len(mid.tracks)])


            for i, track in enumerate(mid.tracks):
                ptrack = ParserTrack(track, mid.ticks_per_beat)
                pretty_table.add_row(["", ""])
                default = ""
                if ptrack.signature.time_is_default:
                    default = " *D"
                pretty_table.add_row(["Track Name", ptrack.name])
                pretty_table.add_row(["Ticks Per Beat", ptrack.signature.mid_ticks_per_beat])
                pretty_table.add_row(["Time Signature{0}".format(default), ptrack.signature.time_signature])
                pretty_table.add_row(["Clocks Per Click{0}".format(default), ptrack.signature.time_clocks_per_click])
                pretty_table.add_row(["Notated 32nd notes per beat{0}".format(default), ptrack.signature.time_32nds_per_beat])
                pretty_table.add_row(["Track Notes (4bars format)".format(default), ptrack.track_string])

            print(pretty_table)
            print()


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
